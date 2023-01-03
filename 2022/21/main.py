class Monkey(object):

    def __init__(self, value=0, dependencies=""):
        self.value = value
        self.dependencies = dependencies

    @classmethod
    def parse(cls, monkey_str):
        if monkey_str.isnumeric():
            return cls(
                value=int(monkey_str)
            )
        return cls(dependencies=monkey_str)

    def get_value(self, monkey_list):
        if self.value > 0:
            return self.value
        parts = self.dependencies.split(" ")

        return eval(str(monkey_list[parts[0]].get_value(monkey_list)) + parts[1] + str(monkey_list[parts[2]].get_value(monkey_list)))


if __name__ == "__main__":
    with open("input_test.txt", "r") as file:
        input_raw = file.read().splitlines()

    monkeys = {
        line.split(": ")[0]: Monkey.parse(line.split(": ")[1])
        for line in input_raw
    }
    print(monkeys["root"].get_value(monkeys))

