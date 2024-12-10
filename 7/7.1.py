if __name__ == "__main__":
    file = open("input.txt")
    rows = file.readlines()
    overall_sum = 0
    for r, row in enumerate(rows):
        result = int(row.split(': ')[0])
        values = [int(v) for v in row.strip().split(': ')[1].split(' ')]

        # print(f'{result}: {values}')

        possible_res = [values[0]]
        for v in values[1:]:
            l = len(possible_res)
            for i in range(l):
                possible_res.append(v+possible_res[i])
                possible_res.append(v*possible_res[i])
            possible_res = possible_res[l:]
        if result in possible_res:
            overall_sum += result

    print(overall_sum)




