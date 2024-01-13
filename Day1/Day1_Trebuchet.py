import re

dic = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def get_num(text_file_title="Day1_Trebuchet.txt"):
    # starts_with = "^[a-zA-z\s.]*([0-9])"
    # ends_with = "([0-9])[a-zA-z]*$"
    regexes = "(\d)"

    text_file = open(text_file_title, "r")
    summ = 0

    while (True):
        line = text_file.readline()
        if not line:
            break
        try:
            summ += num_to_sum(line, regexes)
        except Exception as e:
            print(e)
    return summ


def get_num_w_letters(text_file_title="Day1_Trebuchet.txt"):
    regexes = "(?=(one|two|three|four|five|six|seven|eight|nine|\d))"

    text_file = open(text_file_title, "r")
    summ = 0

    while (True):
        line = text_file.readline()
        if not line:
            break
        try:
            summ += num_to_sum(line, regexes)
        except Exception as e:
            print(e)
    return summ


def num_to_sum(line, regexes):
    try:
        first_dig = re.findall(regexes, line)[0]
        last_dig = re.findall(regexes, line)[-1]
        if len(first_dig) > 1:
            first_dig = dic[first_dig]
        if len(last_dig) > 1:
            last_dig = dic[last_dig]
    except Exception as e:
        print(e)
    return int(first_dig) * 10 + int(last_dig)


if __name__ == '__main__':
    print(get_num())
    print(get_num_w_letters())
