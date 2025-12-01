import sys


def main(filename):
    rotations = []
    with open(filename, "r") as f:
        for line in f.readlines():
            rotations.append((line[0], int(line[1:])))

    num_zeros = 0
    position = 50
    for direction, amount in rotations:
        if direction == "L":
            # "flip" this scenario to turn it into the equivalent rightwards rotation
            flipped_position = (100 - position) % 100
            num_zeros += (flipped_position + amount) // 100

            position -= amount
        elif direction == "R":
            num_zeros += (position + amount) // 100

            position += amount
        else:
            raise Exception(f"invalid direction: {direction}")

        position = position % 100

    print(num_zeros)


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print("must provide a filename")
        sys.exit(1)

    main(filename)
