import re

if __name__ == "__main__":
    file = open("input.txt")
    lines = file.read()

    sum = 0
    matches = re.findall(r"(do\(\)|don't\(\))|mul\((\d{1,3}),(\d{1,3})\)", lines, re.MULTILINE)

    skip = False
    for match in matches:
        if match[0] == "don't()":
            skip = True
            continue
        elif match[0] == "do()":
            skip = False
            continue
        else:
            if not skip:
                sum += int(match[1]) * int(match[2])

    print(sum)
