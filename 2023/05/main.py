def read_seeds_v1(line):
    parts = line.split(": ")
    return [
        int(elem)
        for elem in parts[1].split(" ")
    ]


def read_seeds_v2(line):
    parts = line.split(": ")
    seeds_nums = parts[1].split(" ")
    seeds_nums_ret = []
    for i in range(0, len(seeds_nums), 2):
        seeds_nums_ret.extend([int(seeds_nums[i]) + j for j in range(0, int(seeds_nums[i+1]), 20048)])
    return seeds_nums_ret


def read_map(input_raw):
    return [
        list(map(int, line.split(" ")))
        for line in input_raw
    ]


def find_next(starting, elem_map):
        for line in elem_map:
            if starting in range(line[1], line[1] + line[2]):
                return line[0] + (starting - line[1])
        return starting


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_raw = file.read().splitlines()

    seeds = read_seeds_v1(input_raw[0])
    # seeds = read_seeds_v2(input_raw[0])

    line_count = 2
    next_break = line_count + input_raw[line_count:].index("")
    seed_soil_map = read_map(input_raw[line_count+1:next_break])

    soil = [
        find_next(elem, seed_soil_map)
        for elem in seeds
    ]

    line_count = next_break + 1
    next_break = line_count + input_raw[line_count:].index("")
    soil_fertilizer_map = read_map(input_raw[line_count+1:next_break])

    fertilizer = [
        find_next(elem, soil_fertilizer_map)
        for elem in soil
    ]

    line_count = next_break + 1
    next_break = line_count + input_raw[line_count:].index("")
    fertilizer_water_map = read_map(input_raw[line_count + 1:next_break])

    water = [
        find_next(elem, fertilizer_water_map)
        for elem in fertilizer
    ]

    line_count = next_break + 1
    next_break = line_count + input_raw[line_count:].index("")
    water_light_map = read_map(input_raw[line_count + 1:next_break])

    light = [
        find_next(elem, water_light_map)
        for elem in water
    ]

    line_count = next_break + 1
    next_break = line_count + input_raw[line_count:].index("")
    light_temperature_map = read_map(input_raw[line_count + 1:next_break])

    temperature = [
        find_next(elem, light_temperature_map)
        for elem in light
    ]

    line_count = next_break + 1
    next_break = line_count + input_raw[line_count:].index("")
    temperature_humidity_map = read_map(input_raw[line_count + 1:next_break])

    humidity = [
        find_next(elem, temperature_humidity_map)
        for elem in temperature
    ]

    line_count = next_break + 1
    humidity_location_map = read_map(input_raw[line_count + 1:])

    location = [
        find_next(elem, humidity_location_map)
        for elem in humidity
    ]

    # print(location)
    print(min(location))
