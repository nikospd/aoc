def read_input(name: str, debug: bool = False):
    file_name = ""
    if debug:
        file_name = "examples/{}.txt".format(name)
    else:
        file_name = "inputs/{}.txt".format(name)
    with open(file_name, "r") as file:
        return file.read().splitlines()