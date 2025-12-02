import sys


def is_invalid_id(id):
    str_id = str(id)
    first_half = str_id[: len(str_id) // 2]
    second_half = str_id[len(str_id) // 2 :]
    return first_half == second_half


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
