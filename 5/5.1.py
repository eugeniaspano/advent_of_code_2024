if __name__ == "__main__":
    file = open("input.txt")
    lines = file.readlines()

    i = lines.index('\n')
    page_ordering_rules = [line.strip() for line in lines[:i]]
    pages = [line.strip() for line in lines[i+1:]]

    print(pages)
    print(page_ordering_rules)

    sum = 0
    for p in pages:
        page_numbers = p.split(',')

        correct_order = True
        for rule in page_ordering_rules:
            page_before = rule.split('|')[0]
            page_after = rule.split('|')[1]
            if page_before in p and page_after in p:
                if p.find(page_before) > p.find(page_after):
                    correct_order = False
                    break
        if correct_order:
            sum += int(page_numbers[len(page_numbers)//2])

    print(sum)




