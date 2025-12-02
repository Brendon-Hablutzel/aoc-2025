import sys


def is_invalid_id(id):
    str_id = str(id)
    for possible_repeater_len in range(1, len(str_id) // 2 + 1):
        if len(str_id) % possible_repeater_len != 0:
            continue

        all_match = True

        repeater = str_id[:possible_repeater_len]
        for start_pos in range(len(str_id) // possible_repeater_len):
            substr = str_id[
                start_pos * possible_repeater_len : (start_pos * possible_repeater_len)
                + possible_repeater_len
            ]
            if repeater != substr:
                all_match = False
                break

        if all_match:
            return True

    return False


def main(filename):
    content = ""
    with open(filename, "r") as f:
        for line in f.readlines():
            content += line

    ranges = [
        (int(range[0]), int(range[1]))
        for range in map(lambda range: range.split("-"), content.split(","))
    ]

    total = 0
    for start, end in ranges:
        for num in range(start, end + 1):
            if is_invalid_id(num):
                total += num

    print(total)


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print("must provide a filename")
        sys.exit(1)

    main(filename)
