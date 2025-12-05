import sys

from intervals import Interval


def main(filename):
    intervals: list[Interval] = []

    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.rstrip()
            if len(line) == 0:
                # intervals are over
                break

            splitted = line.split("-")
            intervals.append(Interval(int(splitted[0]), int(splitted[1])))

    intervals.sort(key=lambda interval: interval.low)

    i = 0
    while i < len(intervals):
        try:
            first = intervals[i]
            next = intervals[i + 1]

            merged = first.merge(next)
            if merged is not None:
                intervals.pop(i)
                intervals[i] = merged
            else:
                i += 1
        except IndexError:
            break

    total_interval_len = 0
    for interval in intervals:
        total_interval_len += interval.high - interval.low + 1

    print(total_interval_len)


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print("must provide a filename")
        sys.exit(1)

    main(filename)
