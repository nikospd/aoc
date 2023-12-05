def part_one(lines):
    possible_games = 0
    for line in lines:
        parts = line.split(": ")
        game_id = int(parts[0][5:])
        sets = parts[1].split("; ")
        possible_flag = True
        for _set in sets:
            parts = _set.split(", ")
            for part in parts:
                sb = part.split(" ")
                if int(sb[0]) > game_limits[sb[1]]:
                    possible_flag = False
        if possible_flag:
            possible_games += game_id

    return possible_games


def part_tow(lines):
    total_power = 0
    for line in lines:
        parts = line.split(": ")
        sets = parts[1].split("; ")
        score = {"red": 0, "green": 0, "blue": 0}
        for _set in sets:
            parts = _set.split(", ")
            for part in parts:
                sb = part.split(" ")
                if int(sb[0]) > score[sb[1]]:
                    score[sb[1]] = int(sb[0])
        power = score["red"] * score["green"] * score["blue"]
        total_power += power

    return total_power


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_raw = file.read().splitlines()

    game_limits = {"red": 12, "green": 13, "blue": 14}

    print(part_one(input_raw))
    print(part_tow(input_raw))
