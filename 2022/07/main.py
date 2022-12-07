from dataclasses import dataclass
from typing import List
from functools import lru_cache


@dataclass
class File:
    _size: int
    _name: str

    def __hash__(self):
        return hash(frozenset(self.__dict__))

    def size(self):
        return self._size


@dataclass
class Directory:
    _name: str
    _items = List

    def __init__(self, name):
        self._name = name
        self._items = []

    def __hash__(self):
        return hash(frozenset(self.__dict__))

    def add(self, item):
        self._items.append(item)

    @lru_cache(maxsize=20)
    def size(self):
        sum = 0
        for item in self._items:
            sum += item.size()
        return sum


def change_directory(sub, working_directory):
    if sub == "..":
        return "/".join(working_directory.split("/")[:-1]) or "/"

    else:
        if working_directory == "":
            return "/"
        elif working_directory == "/":
            return working_directory + sub
        else:
            return working_directory + "/" + sub


def sum_up_files(directories, limit):
    total_size = 0
    for dir in directories:
        dir_size = directories[dir].size()
        if dir_size <= limit:
            total_size += dir_size
    return total_size


def sort_dir_sizes(directories):
    sizes = []
    for dir in directories:
        sizes.append(directories[dir].size())
    sizes.sort()
    return sizes

def find_file_to_delete(directories):
    unused_space = 70000000 - directories["/"].size()
    space_to_delete = 30000000 - unused_space
    sorted_sizes = sort_dir_sizes(directories)
    for size in sorted_sizes:
        if size > space_to_delete:
            return size


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_raw = file.read().splitlines()
    directories = {
        "/": Directory("/")
    }
    program_counter = 0
    wd = ""
    while program_counter < len(input_raw):
        if input_raw[program_counter] == "$ ls":
            directory = directories[wd]
            program_counter += 1
            while program_counter < len(input_raw) and input_raw[program_counter][0] != "$":
                info = input_raw[program_counter].split(" ")
                if info[0] == "dir":
                    if change_directory(info[1], wd) in list(directories.keys()):
                        print(change_directory(info[1], wd), program_counter)
                    new_dir = Directory(change_directory(info[1], wd))
                    directories[change_directory(info[1], wd)] = new_dir
                    directory.add(new_dir)
                else:
                    directory.add(File(int(info[0]), info[1]))
                program_counter += 1
        if program_counter < len(input_raw) and input_raw[program_counter][0:4] == "$ cd":
            wd2 = (input_raw[program_counter][5:])
            wd = change_directory(input_raw[program_counter][5:], wd)
        program_counter += 1

    # print(sum_up_files(directories, 100000))

    print(find_file_to_delete(directories))

