from pathlib import Path
from utils import  read_input


def part_1(line: str) -> None:
    expanded_map = expand_map(line)
    print("".join(map(str, expanded_map)))
    rearrange_blocks(expanded_map)
    print("".join(map(str, expanded_map)))
    checksum(expanded_map)


def part_2(line: str) -> None:
    expanded_map = expand_map(line)
    spaces_map = find_spaces(expanded_map)
    print(spaces_map)
    rearrange_files(expanded_map, spaces_map)
    print(expanded_map)


def rearrange_files(file_map: list[int], space_map: dict[int, int]) -> None:
    end = len(file_map) - 1
    while file_map[end] != 0:
        if file_map[end] != -1:
            end_file = end
            while file_map[end] == file_map[end - 1]:
                end -= 1
            len_file = end_file - end + 1
            empty_index = next((key for key, value in space_map.items() if value >= len_file), None)
            if not empty_index:
                end -= 1
                continue
            empty_space = space_map[empty_index]
            for i in range(len_file):
                tmp = file_map[empty_index + i]
                file_map[empty_index + i] = file_map[end + i]
                file_map[end + i] = tmp
            # Add the free spaces from the swap into the space_map
            del space_map[empty_index]
            if empty_space > len_file:
                space_map[empty_index + len_file] = empty_space - len_file
            print(file_map)
        else:
            end -= 1



def find_spaces(file_map: list[int]) -> dict[int, int]:
    space_map = {}
    i = 0
    while i < len(file_map):
        if file_map[i] == -1:
            start = i
            while file_map[i] == -1:
                i += 1
            space_map[start] = i - start
        i += 1
    return space_map

def expand_map(line: str) -> list[int]:
    expanded_map = []
    for i in range(len(line)):
        if i%2:
            for j in range(int(line[i])):
                expanded_map.append(-1)
        else:
            for j in range(int(line[i])):
                expanded_map.append(i//2)
    return expanded_map

def rearrange_blocks(file_map: list[int]) -> None:
    start = 0
    end = len(file_map) - 1
    while start < end:
        if file_map[end] != -1:
            while file_map[start] != -1:
                start += 1
            tmp = file_map[end]
            file_map[end] = file_map[start]
            file_map[start] = tmp
        else:
            end -= 1
    tmp = file_map[end]
    file_map[end] = file_map[start]
    file_map[start] = tmp

def checksum(file_map: list[int]) -> None:
    sum = 0
    for i in range(file_map.index(-1)):
        sum += i * file_map[i]
    print(sum)


if __name__ == "__main__":
    lines = read_input(Path(__file__).stem, True)
    # part_1(lines[0])
    part_2(lines[0])