def check_unique(str):
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            if str[i] == str[j]:
                return False
    return True


def find_first_marker(stream):
    for idx, _ in enumerate(stream):
        if check_unique(stream[idx:idx + 4]):
            return idx + 4
    return 0


def find_first_message(stream):
    for idx, _ in enumerate(stream):
        if check_unique(stream[idx:idx + 14]):
            return idx + 14
    return 0


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_stream = file.read().splitlines()
    # first_marker = find_first_marker(input_stream[0])
    # print(first_marker)
    first_message = find_first_message(input_stream[0])
    print(first_message)
