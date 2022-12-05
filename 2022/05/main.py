def read_stacks():
    with open("d5_stacks.txt", "r") as file:
        stacks_raw = file.read().splitlines()

    tmp_stacks = [[] for i in range(9)]
    for line in stacks_raw:
        for idx, char in enumerate(line):
            if char not in " []":
                tmp_stacks[idx//4].append(char)
    return tmp_stacks


def rearrange_stacks(input_stacks):
    with open("input_moves.txt", "r") as file:
        moves_raw = file.read().splitlines()
    for move in moves_raw:
        parts = move.split(" ")
        num_of_stacks = int(parts[1])
        idx_from = int(parts[3])
        idx_to = int(parts[5])
        for _ in range(num_of_stacks):
            input_stacks[idx_to-1].insert(
                0,
                input_stacks[idx_from-1].pop(0)
            )


def rearrange_stacks_v2(input_stacks):
    with open("input_moves.txt", "r") as file:
        moves_raw = file.read().splitlines()
    for move in moves_raw:
        parts = move.split(" ")
        num_of_stacks = int(parts[1])
        idx_from = int(parts[3])
        idx_to = int(parts[5])
        for i in range(num_of_stacks):
            input_stacks[idx_to-1].insert(
                i,
                input_stacks[idx_from-1].pop(0)
            )


if __name__ == "__main__":
    stacks = read_stacks()
    print(stacks)
    rearrange_stacks_v2(stacks)
    print(stacks)

    print("".join([
        stack[0]
        for stack in stacks
    ]))
