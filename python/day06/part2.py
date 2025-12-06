import sys


def main(filename):
    inputs = []
    operators = []
    with open(filename, "r") as f:
        reading_inputs = True
        for line in f.readlines():
            line = line.rstrip()
            if line.startswith("+") or line.startswith("*"):
                reading_inputs = False

            if reading_inputs:
                inputs.append(line)
            else:
                operators = line

    # so that we can detect that the last operation is over by checking for a
    # column of all spaces, instead of end of line
    for i in range(len(inputs)):
        inputs[i] += " "

    biggest = max(len(line) for line in inputs)

    total = 0
    current_operator = operators[0]
    current_operation_total = 0
    for i in range(biggest):
        input_chars = []
        for line in inputs:
            try:
                input_chars.append(line[i])
            except IndexError:
                input_chars.append(" ")

        try:
            operator_char = operators[i]
            if operator_char != " ":
                current_operator = operator_char
        except IndexError:
            pass

        if all(input_char == " " for input_char in input_chars):
            total += current_operation_total
            current_operation_total = 0
        else:
            input_num = int(
                "".join(input_char for input_char in input_chars if input_char != " ")
            )
            if current_operator == "+":
                current_operation_total += input_num
            elif current_operator == "*":
                if current_operation_total == 0:
                    current_operation_total = 1
                current_operation_total *= input_num
            else:
                raise Exception(f"invalid operator: {current_operator}")

    print(total)


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print("must provide a filename")
        sys.exit(1)

    main(filename)
