import sys

# dial has numbers 0 through 99 (inclusive)
#
# left => lower numbers
# right => higher numbers
#
# dial begins at 50

# start at 98
# R1 (99)
# R1 (0)
# R3 (3)
# L2 (1)


def main(filename):
    rotations = []
    with open(filename, "r") as f:
        for line in f.readlines():
            rotations.append((line[0], int(line[1:])))

    num_zeros = 0
    position = 50
    for direction, amount in rotations:
        if direction == "L":
            position -= amount
        elif direction == "R":
            position += amount
        else:
            raise Exception(f"invalid direction: {direction}")

        position = position % 100
        if position == 0:
            num_zeros += 1

    print(num_zeros)


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print("must provide a filename")
        sys.exit(1)

    main(filename)
