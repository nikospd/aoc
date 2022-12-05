def find_shape(opponent: str, strategy: str) -> str:
    # TODO: maybe add an enum to match paper, rock, scissor to make it less hardcoded
    if (opponent == "A" and strategy == "X") or (opponent == "C" and strategy == "Y") or (opponent == "B" and strategy == "Z"):
        return "Z"
    if (opponent == "C" and strategy == "X") or (opponent == "B" and strategy == "Y") or (opponent == "A" and strategy == "Z"):
        return "Y"
    return "X"


def match_points(house: str, opponent: str) -> int:
    if (house == "A" and opponent == "Z") or (house == "B" and opponent == "X") or (house == "C" and opponent == "Y"):
        return 0
    if (house == "C" and opponent == "X") or (house == "A" and opponent == "Y") or (house == "B" and opponent == "Z"):
        return 6
    return 3


def shape_points(shape: str) -> int:
    if shape == "X":
        return 1
    if shape == "Y":
        return 2
    if shape == "Z":
        return 3


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        hands = file.read().splitlines()
    sum_points = 0
    for hand in hands:
        [house_shape, strategy] = hand.split(" ")
        opponent_shape = find_shape(house_shape, strategy)
        sum_points += (match_points(house_shape, opponent_shape) + shape_points(opponent_shape))
    print(sum_points)

