import sys


def max_digit_index_from_string(s):
    max_value = 0
    max_idx = -1
    for i, digit in enumerate(s):
        num = int(digit)
        # we want the first max value
        if num > max_value:
            max_value = num
            max_idx = i
    return max_idx


def largest_n_digit_number(bank, num_digits_remaining, current_num):
    if num_digits_remaining == 0:
        return current_num

    # let's say we have 8 in the bank and we're making a 6 digit number:
    # for the first digit, we can select from the first 3 characters (we have 8 characters total; after selecting
    # this digit, we need 5 more, so 3 = 8 - (6 - 1))
    to_select_from = bank[: len(bank) - (num_digits_remaining - 1)]
    largest_idx = max_digit_index_from_string(to_select_from)
    largest_val = int(to_select_from[largest_idx])
    new_num = current_num * 10 + largest_val

    return largest_n_digit_number(
        bank[largest_idx + 1 :], num_digits_remaining - 1, new_num
    )


def max_joltage_from_bank(bank):
    return largest_n_digit_number(bank, 12, 0)


def main(filename):
    total = 0

    with open(filename, "r") as f:
        for bank in f.readlines():
            bank = bank.rstrip()
            max_joltage = max_joltage_from_bank(bank)
            total += max_joltage

    print(total)


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print("must provide a filename")
        sys.exit(1)

    main(filename)
