import re

if __name__ == "__main__":
    file = open("input.txt")
    lines = file.read()

    sum = 0
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", lines, re.MULTILINE)

    for match in matches:
        sum += int(match[0]) * int(match[1])

    print(sum)
