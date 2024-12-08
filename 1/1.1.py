if __name__ == "__main__":
    file = open("input.txt")
    lines = file.readlines()

    column_one = []
    column_two = []

    for l in lines:
        first_number = l.split('   ')[0]
        second_number = l.split('   ')[1]

        column_one.append(int(first_number))
        column_two.append(int(second_number))

    sum_distances = 0
    while len(column_one) > 0:
        sum_distances += abs(min(column_one) - min(column_two))
        column_one.remove(min(column_one))
        column_two.remove(min(column_two))

    print(sum_distances)
