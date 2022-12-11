from typing import Sequence, Mapping
import json
import time
import math
import cProfile


class Monkey:
    idx: int
    items: Sequence[int]
    operation: Mapping[str, int]
    test: Mapping[str, int]

    def __init__(self, idx, monkey_str):
        self.idx = idx
        self.parse_items(monkey_str[1])
        self.parse_operation(monkey_str[2])
        self.parse_test(monkey_str[3:])

    def parse_items(self, items_str):
        self.items = json.loads("[" + items_str.split(": ")[1] + "]")

    def parse_operation(self, operation_str):
        operation_str = operation_str.split("= ")[1]
        parts = operation_str.split(" ")
        if parts[1] == "+":
            self.operation = {"operator": 1, "operand": int(parts[2])}
        else:
            if parts[2] == "old":
                self.operation = {"operator": 2, "operand": 0}
            else:
                self.operation = {"operator": 2, "operand": int(parts[2])}

    def parse_test(self, test_str):
        self.test = {
            "limit": int(test_str[0].split("by ")[1]),
            "pass": int(test_str[1].split("monkey ")[1]),
            "fail": int(test_str[2].split("monkey ")[1])
        }

    def operate(self, value) -> int:
        if self.operation["operator"] == 1:
            return value + self.operation["operand"]
        else:
            if self.operation["operand"] == 0:
                return value ** 2
            else:
                return value * self.operation["operand"]

    def do_test(self, value) -> int:
        if value % self.test["limit"]:
            return self.test["fail"]
        else:
            return self.test["pass"]


def parse_monkeys(monkeys, input_raw):
    for i in range(0, len(input_raw), 7):
        monkeys.append(Monkey(i//7, input_raw[i:i+6]))


def calculate(monkeys, inspections, rounds, lcm):
    for i in range(rounds):
        for monkey in monkeys:
            for _ in range(len(monkey.items)):
                inspections[monkey.idx] += 1
                if lcm is None:
                    stress = monkey.operate(monkey.items.pop(0)) // 3
                else:
                    stress = monkey.operate(monkey.items.pop(0)) % lcm
                monkeys[monkey.do_test(stress)].items.append(stress)


if __name__ == "__main__":
    start_time = time.time()
    with open("input.txt", "r") as file:
        input_raw = file.read().splitlines()
    monkeys = []
    parse_monkeys(monkeys, input_raw)
    inspections = [0] * len(monkeys)
    lcm = math.prod(monkey.test["limit"] for monkey in monkeys)
    calculate(monkeys, inspections, 10000, lcm)
    inspections.sort(reverse=True)
    print(inspections[0] * inspections[1])
    print("--- %s seconds ---" % (time.time() - start_time))
