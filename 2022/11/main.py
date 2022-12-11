from typing import Sequence, Mapping
import json
import time
import math


class Monkey:
    idx: int
    items: Sequence[int]
    operation: str
    test: Mapping[str, int]

    def __init__(self, idx, monkey_str):
        self.idx = idx
        self.parse_items(monkey_str[1])
        self.parse_operation(monkey_str[2])
        self.parse_test(monkey_str[3:])

    def parse_items(self, items_str):
        self.items = json.loads("[" + items_str.split(": ")[1] + "]")

    def parse_operation(self, operation_str):
        self.operation = operation_str.split("= ")[1]

    def parse_test(self, test_str):
        self.test = {
            "limit": int(test_str[0].split("by ")[1]),
            "pass": int(test_str[1].split("monkey ")[1]),
            "fail": int(test_str[2].split("monkey ")[1])
        }

    def operate(self, value) -> int:
        return eval(self.operation.replace("old", str(value)))

    def do_test(self, value) -> int:
        if value % self.test["limit"]:
            return self.test["fail"]
        else:
            return self.test["pass"]


def parse_monkeys(monkeys, input_raw):
    for i in range(0, len(input_raw), 7):
        monkeys.append(Monkey(i//7, input_raw[i:i+6]))


if __name__ == "__main__":
    start_time = time.time()
    with open("input_test.txt", "r") as file:
        input_raw = file.read().splitlines()
    monkeys = []
    parse_monkeys(monkeys, input_raw)
    inspections = [0] * len(monkeys)
    num_of_rounds = 1000
    for i in range(num_of_rounds):
        for monkey in monkeys:
            for _ in range(len(monkey.items)):
                inspections[monkey.idx] += 1
                stress = monkey.operate(monkey.items.pop(0)) // 3
                monkeys[monkey.do_test(stress)].items.append(stress)
        if not (i+1) % 20 and i+1 >= 20:
            print("Round: ", i)
            print(inspections)

    inspections.sort(reverse=True)
    print(inspections[0] * inspections[1])
    print("--- %s seconds ---" % (time.time() - start_time))
