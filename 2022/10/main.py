def find_signal_strengths(input_raw):
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
    return sum(signal_strengths)


def calculate_crt(input_raw):
    crt = [
        []
        for i in range(6)
    ]
    cycles = 0
    x = 1
    for command in input_raw:
        if command == "noop":
            if abs((cycles % 40) - x) < 2:
                crt[cycles // 40].append("#")
            else:
                crt[cycles // 40].append(".")
            cycles += 1
            if cycles == 240:
                break
        else:
            for i in range(2):
                if abs((cycles % 40) - x) < 2:
                    crt[cycles // 40].append("#")
                else:
                    crt[cycles // 40].append(".")
                cycles += 1
                if cycles == 240:
                    break
            x += int(command.split(" ")[1])
    return crt

def print_crt(crt):
    for line in crt:
        print(line)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_raw = file.read().splitlines()
    print(find_signal_strengths(input_raw))

    print_crt(calculate_crt(input_raw))
