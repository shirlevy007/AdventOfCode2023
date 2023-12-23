import re

MAX_BLUE = 14
MAX_GREEN = 13
MAX_RED = 12

dic = {"blue": MAX_BLUE, "green": MAX_GREEN, "red": MAX_RED}


def valid_reg(single_output):
    return dic[single_output[2]] >= int(single_output[1])


def valid_games(text_file_title="Day2_CubeConundrum.txt"):

    game_regex = "Game (\d+):"
    regexes = " ((\d+) (blue|green|red+))[,;\s]"

    text_file = open(text_file_title, "r")
    summ = 0

    while (True):
        line = text_file.readline()
        if not line:
            break
        try:
            game_num = int(re.findall(game_regex, line)[0])
            outputs = re.findall(regexes, line)
            for output in outputs:
                if not valid_reg(output):
                    break
            else:
                summ += game_num

        except Exception as e:
            print(e)
    return summ


def min_amounts(outputs):
    min_dic = {"blue": 0, "green": 0, "red": 0}
    for output in outputs:
        min_dic[output[2]] = max(int(output[1]), min_dic[output[2]])

    return min_dic["blue"] * min_dic["green"] * min_dic["red"]



def min_amounts_powers(text_file_title="Day2_CubeConundrum.txt"):

    regexes = " ((\d+) (blue|green|red+))[,;\s]"

    text_file = open(text_file_title, "r")
    summ = 0

    while (True):
        line = text_file.readline()
        if not line:
            break
        try:
            outputs = re.findall(regexes, line)
            summ += min_amounts(outputs)

        except Exception as e:
            print(e)
    return summ

if __name__ == '__main__':
    # print(valid_games("Day2_CubeConundrum2.txt"))   # 8
    # print(valid_games())    # 2331
    # print(min_amounts_powers("Day2_CubeConundrum2.txt"))    # 2286
    print(min_amounts_powers())    # 71585
