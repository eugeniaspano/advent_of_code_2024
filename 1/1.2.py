from operator import countOf

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

    sum_similarities = 0
    for item in column_one:
        sum_similarities += item * countOf(column_two, item)

    print(sum_similarities)
