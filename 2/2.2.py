def is_safe(report):
    decreasing = 0
    increasing = 0
    for i, _ in enumerate(report):
        if i + 1 < len(report):
            current_item = int(report[i])
            next_item = int(report[i + 1])
            if abs(current_item - next_item) > 3 or current_item == next_item:
                return False, i
            if current_item - next_item > 0:
                decreasing += 1
                if decreasing > 0 and increasing > 0:
                    return False, i
            else:
                increasing += 1
                if decreasing > 0 and increasing > 0:
                    return False, i
    return True, -1


if __name__ == "__main__":
    file = open("input.txt")
    lines = file.readlines()

    safe = 0
    for line in lines:
        report = line.rstrip().split(' ')

        for i in range(0,len(report)):
            new_report = report[:i] + report[i+1:]
            is_report_safe, _ = is_safe(new_report)
            if is_report_safe:
                safe += 1
                break

    print(safe)



