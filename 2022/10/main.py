if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_raw = file.read().splitlines()
    cycles = 0
    x = 1
    signal_strengths = []
    for command in input_raw:
        addition = 0
        if command == "noop":
            cycles += 1
            if (cycles + 20) % 40 == 0:
                signal_strengths.append(cycles * x)
        else:
            cycles += 2
            if (cycles + 20) % 40 == 0:
                signal_strengths.append(cycles * x)
            if (cycles + 20) % 40 == 1:
                signal_strengths.append((cycles - 1) * x)
            x += int(command.split(" ")[1])
    print(sum(signal_strengths))


