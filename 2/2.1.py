if __name__ == "__main__":
    file = open("input.txt")
    lines = file.readlines()

    safe = len(lines)
    for line in lines:
        decreasing = 0
        increasing = 0
        report = line.rstrip().split(' ')
        for i, level in enumerate(report):
            if i+1 < len(report):
                if abs(int(level) - int(report[i+1])) > 3 or abs(int(level) - int(report[i+1])) == 0:
                    safe -= 1
                    break
                if int(level) - int(report[i+1]) > 0:
                    decreasing += 1
                    if decreasing > 0 and increasing > 0:
                        safe -= 1
                        break
                else:
                    increasing += 1
                    if decreasing > 0 and increasing > 0:
                        safe -= 1
                        break



    print(safe)