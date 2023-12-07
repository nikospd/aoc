def check_tile_v1(x, y, map,width, height):
    if x<0 or x >= width:
        return False
    if y < 0 or y >= height:
        return False
    return map[y][x] != "."


def check_frame_v1(left, right, y, map, width, height):
    for x in range(left, right+1):
        if check_tile_v1(x,y-1,map,width, height):
            return True
        if check_tile_v1(x,y+1,map,width, height):
            return True
    if check_tile_v1(left, y, map,width, height):
        return True
    if check_tile_v1(right, y, map,width, height):
        return True
    return False


def check_tile_v2(x, y, map,width, height):
    if x<0 or x >= width:
        return False
    if y < 0 or y >= height:
        return False
    return map[y][x] == "*"



def check_frame_v2(left, right, y, map, width, height, star_map):
    for x in range(left, right+1):
        if check_tile_v2(x,y-1,map,width, height):
            if star_map.get((x,y-1)):
                star_map[(x,y-1)].extend([map[y][left+1:right]])
            else:
                star_map[(x, y - 1)] = [map[y][left + 1:right]]
        if check_tile_v2(x,y+1,map,width, height):
            if star_map.get((x, y + 1)):
                star_map[(x, y + 1)].extend([map[y][left + 1:right]])
            else:
                star_map[(x, y + 1)] = [map[y][left + 1:right]]
    if check_tile_v2(left, y, map,width, height):
        if star_map.get((left, y)):
            star_map[(left, y)].extend([map[y][left + 1:right]])
        else:
            star_map[(left, y)] = [map[y][left + 1:right]]
    if check_tile_v2(right, y, map,width, height):
        if star_map.get((right, y)):
            star_map[(right, y)].extend([map[y][left + 1:right]])
        else:
            star_map[(right, y)] = [map[y][left + 1:right]]

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_raw = file.read().splitlines()

    width = len(input_raw[0])
    height = len(input_raw)

    engine_sum = 0
    star_map = {}
    j = 0
    while j < height:
        i = 0
        while i < width:
            if input_raw[j][i].isdigit():
                y = j
                x1 = i
                while i < width and input_raw[j][i].isdigit():
                    i += 1
                    pass
                x2 = i
                if(check_frame_v1(x1-1, x2, y, input_raw, width, height)):
                    engine_sum += int(input_raw[y][x1:x2])
                check_frame_v2(x1 - 1, x2, y, input_raw, width, height, star_map)
            i += 1
        j += 1
    print(engine_sum)
    star_sum = 0
    for v in star_map.values():
        if len(v) == 2:
            star_sum += int(v[0]) * int(v[1])
    print(star_sum)
