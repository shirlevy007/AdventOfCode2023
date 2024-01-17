import re
import copy


def winnings_in_card(winning_numbers, numbers_to_check):
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
    return summ


def add_to_card_dict(cards_dict, card_num, winning_numbers, numbers_to_check):
    cards_dict[card_num] = (winning_numbers, numbers_to_check, winnings_in_card(winning_numbers, numbers_to_check))


def split_sort_output(output):
    winning_numbers = output[0].split()
    winning_numbers = sorted(int(number) for number in winning_numbers)
    numbers_to_check = output[1].split()
    numbers_to_check = sorted(int(number) for number in numbers_to_check)
    return winning_numbers, numbers_to_check


def valid_card(text_file="Day4_Scratchcards.txt", part1=True):
    card_regex = "Card\s+(\d+):"
    regexes = "([\d+\s]+)\|\s([\d+\s+]+)"

    text_file = open(text_file, "r")
    summ = 0

    if not part1: cards_dict = {}

    line = text_file.readline()
    while (line):
        try:
            card_num = int(re.findall(card_regex, line)[0])
            outputs = re.findall(regexes, line)
            winning_numbers, numbers_to_check = split_sort_output(outputs[0])
            if part1:
                res = winnings_in_card(winning_numbers, numbers_to_check)
                summ += 2 ** (res - 1) if res > 0 else 0  # as in instructions
            else:
                add_to_card_dict(cards_dict, card_num, winning_numbers, numbers_to_check)

        except Exception as e:
            print(e)
        line = text_file.readline()

    if part1:
        return summ

    # else:
    count_cards_dict = {}
    count_cards = 0
    for card_num in sorted(cards_dict.keys()):
        count_cards += 1
        for i in range(1,cards_dict[card_num][2]+1):
            if card_num+i in count_cards_dict:
                count_cards_dict[card_num+i] += 1 + (count_cards_dict[card_num] if card_num in count_cards_dict else 0)
            else:
                count_cards_dict[card_num+i] = 1 + (count_cards_dict[card_num] if card_num in count_cards_dict else 0)
        count_cards += count_cards_dict[card_num] if card_num in count_cards_dict else 0
        # winning_numbers, numbers_to_check = cards_dict[card_num]
        # summ += winnings_in_card(winning_numbers, numbers_to_check)
    return count_cards


if __name__ == '__main__':
    print(valid_card())
    print(valid_card(part1=False))
