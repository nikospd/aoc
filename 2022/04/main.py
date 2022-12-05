def fully_contains(worker, compare):
    worker_elems = worker.split("-")
    compare_elems = compare.split("-")
    if int(worker_elems[0]) >= int(compare_elems[0]) and int(worker_elems[1]) <= int(compare_elems[1]):
        return True
    return False


def overlaps(worker, compare):
    worker_elems = worker.split("-")
    compare_elems = compare.split("-")
    if int(worker_elems[0]) <= int(compare_elems[0]) <= int(worker_elems[1]):
        return True
    if int(worker_elems[0]) <= int(compare_elems[1]) <= int(worker_elems[1]):
        return True
    return False


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        assignments = file.read().splitlines()

    count = 0
    for pair in assignments:
        first, second = pair.split(",")
        # if fully_contains(first, second) or fully_contains(second, first):
        if overlaps(first, second) or overlaps(second, first):
            count += 1
    print(count)
