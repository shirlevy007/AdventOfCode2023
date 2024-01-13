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
        symbol_search_begin, symbol_search_end = max(0, output.span()[0] - 1), min(output.span()[1] + 1, len(line) - 1)
        flag_part_num = False
        flag_part_num = is_valid_part_number(line, symbol_search_begin, symbol_search_begin + 1, flag_part_num)
        flag_part_num = is_valid_part_number(line, symbol_search_end - 1, symbol_search_end, flag_part_num)
        flag_part_num = is_valid_part_number(pre_line, symbol_search_begin, symbol_search_end, flag_part_num)
        flag_part_num = is_valid_part_number(post_line, symbol_search_begin, symbol_search_end, flag_part_num)
        if flag_part_num:
            sum_line += int(line[output.span()[0]:output.span()[1]])
    return sum_line


def gear_ratio(text_file_title="Day3_GearRatios.txt", part_one=True):
    gear_reg = "(\*)"
    regexes = "(\d+)"

    text_file = open(text_file_title, "r")
    summ = 0

    pre_line = ""
    line = text_file.readline()
    post_line = text_file.readline()

    while (line):
        try:
            # nums_outputs = re.finditer(regexes, line)
            if part_one:
                outputs = re.finditer(regexes, line)
                summ += sum_valid_part_number(outputs, pre_line, line, post_line)
            else:
                outputs = re.finditer(gear_reg, line)
                summ += sum_valid_gears(outputs, pre_line, line, post_line)
        except Exception as e:
            print(e)
        pre_line, line, post_line = line, post_line, text_file.readline()
    return summ


def sum_valid_gears(outputs, pre_line, line, post_line):
    regexes = "(\d+)"
    sum_line = 0
    for output in outputs:
        symbol_search_begin, symbol_search_end = max(0, output.span()[0] - 1), min(output.span()[1] , len(line) - 1)
        count_nearby_nums = 0
        nums_list=[]
        count_nearby_nums = count_nums_valid_gear(line, symbol_search_begin, min(symbol_search_begin + 1, len(line)-1), count_nearby_nums, nums_list)
        count_nearby_nums = count_nums_valid_gear(line, max(0,symbol_search_end - 1), symbol_search_end, count_nearby_nums, nums_list)
        count_nearby_nums = count_nums_valid_gear(pre_line, symbol_search_begin, symbol_search_end, count_nearby_nums, nums_list)
        count_nearby_nums = count_nums_valid_gear(post_line, symbol_search_begin, symbol_search_end, count_nearby_nums, nums_list)
        if count_nearby_nums==2:
            # print(nums_list, nums_list[0]*nums_list[1])
            sum_line += nums_list[0]*nums_list[1]
    return sum_line


def count_nums_valid_gear(line, star_span_begin, star_span_end, count, nums_list):
    if count > 2:
        return count + 1
    if line:
        reg_num = "(\d+)"
        num_outputs = re.finditer(reg_num, line)
        if num_outputs:
            for num_output in num_outputs:
                if num_output.span()[0] > star_span_end:    # out of * range
                    break
                elif num_output.span()[-1] <= star_span_begin:    # out of * range
                    continue
                else:   # in * range
                    count += 1
                    nums_list.append(int(num_output.group()))
    return count


if __name__ == '__main__':
    print(gear_ratio())
    print(gear_ratio(part_one=False))

# 514969
# 78915902