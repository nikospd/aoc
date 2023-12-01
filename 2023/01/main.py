import re

def char_num_translate(word):
    if word == "one":
        return "1"
    elif word == "two":
        return "2"
    elif word == "three":
        return "3"
    elif word == "four":
        return "4"
    elif word == "five":
        return "5"
    elif word == "six":
        return "6"
    elif word == "seven":
        return "7"
    elif word == "eight":
        return "8"
    elif word == "nine":
        return "9"
    else:
        return word


if __name__ == "__main__":
    word_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    with open("input.txt", "r") as file:
        input_raw = file.read().splitlines()
    # pattern = "[" + "".join(word_list) + "]"
    # pattern = "|".join(map(re.escape, word_list))
    pattern = r'(?=(' + '|'.join(map(re.escape, word_list)) + r'))'


    total = 0
    for line in input_raw:
        match = re.findall(pattern, line)
        print(char_num_translate(match[0]),char_num_translate(match[-1]))
        total += int(char_num_translate(match[0])+char_num_translate(match[-1]))
    print(total)
