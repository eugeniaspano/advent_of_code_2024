def get_initial_position(rows):
    for y, row in enumerate(rows):
        initial_y = y
        if '^' in row:
            initial_x = row.index('^')
            break
    return initial_y, initial_x

def move_up_until_obstacle(rows, current_x, current_y, seen):
    for y in range(current_y, -1, -1):
        if rows[y][current_x] == '#':
            return rows, y+1, current_x, seen
        else:
            seen.add((y, current_x))
    return rows, -1, -1, seen

def move_right_until_obstacle(rows, current_x, current_y, seen):
    for x in range(current_x, len(rows[current_y])):
        if rows[current_y][x] == '#':
            return rows, current_y, x-1, seen
        else:
            seen.add((current_y, x))
    return rows, -1, -1, seen

def move_down_until_obstacle(rows, current_x, current_y, seen):
    for y in range(current_y, len(rows)):
        if rows[y][current_x] == '#':
            return rows, y-1, current_x, seen
        else:
            seen.add((y, current_x))
    return rows, -1, -1, seen

def move_left_until_obstacle(rows, current_x, current_y, seen):
    for x in range(current_x, -1, -1):
        if rows[current_y][x] == '#':
            return rows, current_y, x+1, seen
        else:
            seen.add((current_y, x))
    return rows, -1, -1, seen

def move(rows, x, y, direction, seen):
    if x == -1 and y == -1:
        return seen
    if direction == 'up':
        rows, y, x, seen = move_up_until_obstacle(rows, x, y, seen)
        return move(rows, x, y, 'right', seen)
    elif direction == 'right':
        rows, y, x, seen= move_right_until_obstacle(rows, x, y, seen)
        return move(rows, x, y, 'down', seen)
    elif direction == 'down':
        rows, y, x, seen = move_down_until_obstacle(rows, x, y, seen)
        return move(rows, x, y, 'left', seen)
    else:
        rows, y, x, seen = move_left_until_obstacle(rows, x, y, seen)
        return move(rows, x, y, 'up', seen)

if __name__ == "__main__":
    file = open("input.txt")
    rows = file.readlines()

    initial_y, initial_x = get_initial_position(rows)
    seen = move(rows, initial_x, initial_y, 'up', {(initial_y, initial_x)})

    print(len(seen))
