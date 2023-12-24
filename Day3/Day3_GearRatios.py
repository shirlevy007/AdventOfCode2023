import re


def is_valid_part_number(line, span_begin, span_end, flag):
    if flag:
        return True
    if line:
        reg_symbol = "\W|_"
        not_symbol = "\w|\.|\s"
        for i in range(span_begin, span_end):
            if re.fullmatch(reg_symbol, line[i]) and not re.fullmatch(not_symbol, line[i]):
                return True
    return False

def sum_valid_part_number(outputs, pre_line, line, post_line):

    sum_line = 0
    for output in outputs:
        symbol_search_begin, symbol_search_end = max(0, output.span()[0] - 1), min(output.span()[1] + 1, len(line)-1)
        flag_part_num = False
        flag_part_num = is_valid_part_number(line, symbol_search_begin, symbol_search_begin+1, flag_part_num)
        flag_part_num = is_valid_part_number(line, symbol_search_end-1, symbol_search_end, flag_part_num)
        flag_part_num = is_valid_part_number(pre_line, symbol_search_begin, symbol_search_end, flag_part_num)
        flag_part_num = is_valid_part_number(post_line, symbol_search_begin, symbol_search_end, flag_part_num)
        if flag_part_num:
            print(int(line[output.span()[0]:output.span()[1]]))
            sum_line += int(line[output.span()[0]:output.span()[1]])
    return sum_line


def sum_part_numbers(text_file_title="Day3_GearRatios.txt"):
    regexes = "(\d+)"

    text_file = open(text_file_title, "r")
    summ = 0

    pre_line = ""
    line = text_file.readline()
    post_line = text_file.readline()

    while (line):
        try:
            outputs = re.finditer(regexes, line)
            summ += sum_valid_part_number(outputs, pre_line, line, post_line)
        except Exception as e:
            print(e)
        pre_line, line, post_line = line, post_line, text_file.readline()
    return summ


if __name__ == '__main__':
    # print(sum_part_numbers("Day3_GearRatios2.txt"))
    print(sum_part_numbers("Day3_GearRatios.txt"))  # 525911
