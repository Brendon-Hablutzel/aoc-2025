import math
import sys


def main(filename):
    inputs = []
    operators = []
    with open(filename, "r") as f:
        reading_inputs = True
        for line in f.readlines():
            if line.startswith("+") or line.startswith("*"):
                reading_inputs = False

            if reading_inputs:
                inputs.append([int(num) for num in line.rstrip().split()])
            else:
                operators = line.rstrip().split()

    total = 0
    for i in range(len(operators)):
        operator = operators[i]
        if operator == "+":
            total += sum(input_line[i] for input_line in inputs)
        elif operator == "*":
            total += math.prod(input_line[i] for input_line in inputs)
        else:
            raise Exception(f"bad operator: {operator}")

    print(total)


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print("must provide a filename")
        sys.exit(1)

    main(filename)
