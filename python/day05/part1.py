import sys

from intervals import Interval, IntervalTree


def main(filename):
    intervals = []
    nums = []

    reading_intervals = True
    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.rstrip()
            if len(line) == 0:
                reading_intervals = False
                continue

            if reading_intervals:
                splitted = line.split("-")
                intervals.append(Interval(int(splitted[0]), int(splitted[1])))
            else:
                nums.append(int(line))

    tree = IntervalTree(intervals)
    total = 0
    for num in nums:
        if tree.contains_point(num):
            total += 1

    print(total)


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print("must provide a filename")
        sys.exit(1)

    main(filename)
