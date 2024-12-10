from collections import defaultdict
from functools import cmp_to_key

def compare(item1, item2):
    if item1 not in rules and item2 not in rules:
        return 0
    elif item1 in rules:
        if item2 in rules[item1]:
            return -1
        return 0
    else:
        if item1 in rules[item2]:
            return 1
        else:
            return 0

if __name__ == "__main__":
    file = open("input.txt")
    lines = file.readlines()

    i = lines.index('\n')
    page_ordering_rules = [line.strip() for line in lines[:i]]
    pages = [line.strip() for line in lines[i+1:]]

    wrong_pages = []
    sum = 0
    for p in pages:
        page_numbers = [int(i) for i in p.split(',')]

        correct_order = True
        for rule in page_ordering_rules:
            page_before = rule.split('|')[0]
            page_after = rule.split('|')[1]
            if page_before in p and page_after in p:
                if p.find(page_before) > p.find(page_after):
                    wrong_pages.append(page_numbers)
                    break

    rules = defaultdict(list)
    for rule in page_ordering_rules:
        page_before = int(rule.split('|')[0])
        page_after = int(rule.split('|')[1])

        rules[page_before].append(page_after)

    print(rules)

    for page in wrong_pages:
        print(page)
        page.sort(key=cmp_to_key(compare))
        print(page)
        sum += int(page[len(page)//2])

    print(sum)