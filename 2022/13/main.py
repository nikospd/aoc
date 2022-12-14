import ast

# 0: True,
# 1: False,
# 2: Continue


def compare(first, second):
    for i in range(len(first)):
        if i == len(second):
            return 1
        elif type(first[i]) == int and type(second[i]) == int:
            if first[i] > second[i]:
                return 1
            if first[i] < second[i]:
                return 0
        elif type(first[i]) == list and type(second[i]) == list:
            flag = compare(
                first[i],
                second[i]
            )
            if flag == 2:
                continue
            else:
                return flag
        elif type(first[i]) == list:
            flag = compare(
                first[i],
                [second[i]]
            )
            if flag == 2:
                continue
            else:
                return flag
        else:
            flag = compare(
                [first[i]],
                second[i]
            )
            if flag == 2:
                continue
            else:
                return flag
    if len(second) > len(first):
        return 0
    return 2

def find_right_order_idx(input_raw):
    sum = 0
    for i in range(0, len(input_raw), 3):
        right_order = compare(
            ast.literal_eval(input_raw[i]),
            ast.literal_eval(input_raw[i + 1]),
        ) == 0
        # print(int(i / 3) + 1, right_order, input_raw[i], input_raw[i + 1])
        if right_order:
            sum += int(i / 3) + 1
    return sum

def decoder_key_signal(input_raw):
    packets = [
        ast.literal_eval(input_raw[i])
        for i in range(len(input_raw))
        if input_raw[i]
    ]
    packets.append([[2]])
    packets.append([[6]])
    swapped = False
    for i in range(len(packets) - 1):
        for j in range(0, len(packets)-i-1):
            if compare(packets[j], packets[j+1]) != 0:
                swapped = True
                packets[j], packets[j+1] = packets[j+1], packets[j]
        if not swapped:
            return
    print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
    return


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_raw = file.read().splitlines()
    # print(find_right_order_idx(input_raw))
    decoder_key_signal(input_raw)
