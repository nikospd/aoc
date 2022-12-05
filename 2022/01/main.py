if __name__ == "__main__":
    with open("input.txt", "r") as file:
        calories = file.read().splitlines()

    elf_counter = 0
    elf_total_calories = [0]
    for line in calories:
        if line:
            elf_total_calories[elf_counter] += int(line)
        else:
            elf_counter += 1
            elf_total_calories.append(0)

    elf_total_calories.sort(reverse=True)
    print(elf_total_calories[0] + elf_total_calories[1] + elf_total_calories[2])
