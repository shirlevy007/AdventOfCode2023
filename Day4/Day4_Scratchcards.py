import re
import copy


def winnigs_in_card(output):
    winning_numbers = output[0].split()
    winning_numbers = sorted(int(number) for number in winning_numbers)
    numbers_to_check = output[1].split()
    numbers_to_check = sorted(int(number) for number in numbers_to_check)
    summ = 0

    w_ind = 0
    for number in numbers_to_check:
        while winning_numbers[w_ind] < number and w_ind < len(winning_numbers) - 1:
            w_ind += 1
        if winning_numbers[w_ind] == number:
            summ += 1
            w_ind += 1
        if w_ind == len(winning_numbers):
            break
    return 2**(summ-1) if summ > 0 else 0



def valid_card(text_file="Day4_Scratchcards.txt"):
    card_regex = "Card\s+(\d+):"
    regexes = "([\d+\s]+)\|\s([\d+\s+]+)"

    text_file = open(text_file, "r")
    summ = 0

    line = text_file.readline()
    while (line):
        try:
            card_num = int(re.findall(card_regex, line)[0])
            outputs = re.findall(regexes, line)
            for output in outputs:
                summ += winnigs_in_card(output)
                # if not valid_reg(output):
                #     break

        except Exception as e:
            print(e)
        line = text_file.readline()
    return summ


if __name__ == '__main__':

    print(valid_card())