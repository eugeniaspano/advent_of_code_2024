
def search_diagonally_up_right(lines, current_x, current_y):
    y = current_y - 1
    x = current_x + 1

    if x < len(lines[current_y]) and y >= 0:
        return lines[y][x]
    else:
        return 'empty'

def search_diagonally_down_right(lines, current_x, current_y):
    y = current_y + 1
    x = current_x + 1

    if x < len(lines[current_y]) and y < len(lines):
        return lines[y][x]
    else:
        return 'empty'

def search_diagonally_down_left(lines, current_x, current_y):
    y = current_y + 1
    x = current_x - 1

    if x >= 0 and y < len(lines):
        return lines[y][x]
    else:
        return 'empty'

def search_diagonally_up_left(lines, current_x, current_y):
    y = current_y - 1
    x = current_x - 1

    if x >= 0 and y >= 0:
        return lines[y][x]
    else:
        return 'empty'


if __name__ == "__main__":
    file = open("input.txt")
    lines = file.readlines()

    count = 0
    for y, line in enumerate(lines):
        for x, character  in enumerate(line.strip()):
            if character == 'A':
                if ((search_diagonally_up_right(lines, x, y) == 'M' and search_diagonally_down_left(lines, x, y) == 'S') or (search_diagonally_up_right(lines, x, y) == 'S' and search_diagonally_down_left(lines, x, y) == 'M')) and ((search_diagonally_up_left(lines, x, y) == 'M' and search_diagonally_down_right(lines, x, y) == 'S') or (search_diagonally_up_left(lines, x, y) == 'S' and search_diagonally_down_right(lines, x, y) == 'M')):
                    count += 1
    print(count)