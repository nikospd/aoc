from sympy import *
from sympy.solvers import solve

class Monkey(object):

    def __init__(self, name, value=0, dependencies=""):
        self.name = name
        self.value = value
        self.dependencies = dependencies

    @classmethod
    def parse(cls, monkey_name, monkey_str):
        if monkey_str.isnumeric():
            return cls(
                name=monkey_name,
                value=int(monkey_str)
            )
        return cls(name=monkey_name, dependencies=monkey_str)

    def get_value(self, monkey_list, eq=False):
        if eq and self.name == "humn":
            return x
        if self.value > 0:
            return self.value
        parts = self.dependencies.split(" ")
        first = monkey_list[parts[0]].get_value(monkey_list, eq)
        second = monkey_list[parts[2]].get_value(monkey_list, eq)
        return eval("(" + str(first) + ")" + parts[1] + "(" + str(second) + ")")

    def find_humn(self, monkey_list):
        parts = self.dependencies.split(" ")
        first = monkey_list[parts[0]].get_value(monkey_list, True)
        second = monkey_list[parts[2]].get_value(monkey_list, True)
        route = eval("(" + str(first) + ") - (" + str(second) + ")")
        return solve(route, x)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_raw = file.read().splitlines()

    monkeys = {
        line.split(": ")[0]: Monkey.parse(line.split(": ")[0], line.split(": ")[1])
        for line in input_raw
    }
    # print(monkeys["root"].get_value(monkeys))

    x = symbols("x")
    print(monkeys["root"].find_humn(monkeys))




