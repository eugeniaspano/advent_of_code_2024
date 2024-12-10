def search_right(lines, current_x, current_y):
    string = lines[current_y][current_x:]
    if string.startswith('XMAS'):
        return True

def search_left(lines, current_x, current_y):
    string = lines[current_y][0:current_x+1]
    if string.endswith('SAMX'):
        return True

def search_down(lines, current_x, current_y):
    string = ''
    for y in range(current_y, len(lines)):
        string += lines[y][current_x]
    if string.startswith('XMAS'):
        return True

def search_up(lines, current_x, current_y):
    string = ''
    for y in range(0, current_y+1):
        string += lines[y][current_x]
    if string.endswith('SAMX'):
        return True

def search_diagonally_up_right(lines, current_x, current_y):
    string = ''
    y_s = range(current_y, -1, -1)
    x_s = range(current_x, len(lines[current_y]))

    for i in range(0, min(len(x_s), len(y_s))):
        string += lines[y_s[i]][x_s[i]]
    if string.startswith('XMAS'):
        return True

def search_diagonally_down_right(lines, current_x, current_y):
    string = ''
    y_s = range(current_y, len(lines))
    x_s = range(current_x, len(lines[current_y]))

    for i in range(0, min(len(x_s), len(y_s))):
        string += lines[y_s[i]][x_s[i]]
    if string.startswith('XMAS'):
        return True

def search_diagonally_down_left(lines, current_x, current_y):
    string = ''
    y_s = range(current_y, len(lines))
    x_s = range(current_x, -1, -1)

    for i in range(0, min(len(x_s), len(y_s))):
        string += lines[y_s[i]][x_s[i]]
    if string.startswith('XMAS'):
        return True

def search_diagonally_up_left(lines, current_x, current_y):
    string = ''
    y_s = range(current_y, -1, -1)
    x_s = range(current_x, -1, -1)

    for i in range(0, min(len(x_s), len(y_s))):
        string += lines[y_s[i]][x_s[i]]
    if string.startswith('XMAS'):
        return True


if __name__ == "__main__":
    file = open("input.txt")
    lines = file.readlines()

    count = 0
    for y, line in enumerate(lines):
        for x, character  in enumerate(line.strip()):
            if character == 'X':
                if search_up(lines, x, y):
                    count += 1
                if search_diagonally_up_right(lines, x, y):
                    count += 1
                if search_right(lines, x, y):
                    count += 1
                if search_diagonally_down_right(lines, x, y):
                    count += 1
                if search_down(lines, x, y):
                    count += 1
                if search_diagonally_down_left(lines, x, y):
                    count += 1
                if search_left(lines, x, y):
                    count += 1
                if search_diagonally_up_left(lines, x, y):
                    count += 1
    print(count)