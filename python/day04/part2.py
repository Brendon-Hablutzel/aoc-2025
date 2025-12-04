import sys


def get(grid, row_idx, col_idx):
    if row_idx < 0 or col_idx < 0:
        return "."
    try:
        return grid[row_idx][col_idx]
    except IndexError:
        return "."


def is_accessible(grid, row_idx, col_idx):
    # start at -1 to account for the roll in the middle
    num_adjacent = -1
    for row_delta in range(-1, 2):
        for col_delta in range(-1, 2):
            if get(grid, row_idx + row_delta, col_idx + col_delta) == "@":
                num_adjacent += 1

    return num_adjacent < 4


def main(filename):
    grid = []
    with open(filename, "r") as f:
        for line in f.readlines():
            grid.append(list(line.rstrip()))

    total_removed = 0
    while True:
        accessible_cells = []
        for row_idx in range(len(grid)):
            for col_idx in range(len(grid[0])):
                if grid[row_idx][col_idx] == "@" and is_accessible(
                    grid, row_idx, col_idx
                ):
                    accessible_cells.append((row_idx, col_idx))

        if len(accessible_cells) == 0:
            break

        total_removed += len(accessible_cells)

        for row_idx, col_idx in accessible_cells:
            grid[row_idx][col_idx] = "."

    print(total_removed)


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print("must provide a filename")
        sys.exit(1)

    main(filename)
