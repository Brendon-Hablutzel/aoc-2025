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


def max_joltage_from_bank(bank):
    first_digit_idx = max_digit_index_from_string(bank[:-1])
    second_digit_idx = (
        first_digit_idx + 1 + max_digit_index_from_string(bank[first_digit_idx + 1 :])
    )
    return int(bank[first_digit_idx] + bank[second_digit_idx])


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
