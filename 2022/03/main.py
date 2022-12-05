def find_errors(pack, items):
    for rucksack in pack:
        [first_half, second_half] = [rucksack[:int(len(rucksack) / 2)], rucksack[int(len(rucksack) / 2):]]
        for letter in first_half:
            if letter in second_half:
                items.append(letter)
                break


def find_badges(pack, items):
    counter = 0
    while counter < len(pack):
        for letter in pack[counter]:
            if (letter in pack[counter+1]) and (letter in pack[counter+2]):
                items.append(letter)
                counter += 3
                break


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        inventory = file.read().splitlines()
    shared_types = []

    # find_errors(inventory, shared_types)
    find_badges(inventory, shared_types)

    priorities = 0
    for item in shared_types:
        if item.isupper():
            priorities += ord(item) - 38
        else:
            priorities += ord(item) - 96
    print(priorities)
