safe = 0

with open('2.txt') as f:
    lines = f.readlines()
    for line in lines:
        reports = list(map(int, line.split()))

        if reports[0] < reports[1]:
            increasing = True
        elif reports[0] > reports[1]:
            increasing = False
        else:
            continue

        line_safe = True
        for i in range(len(reports) - 1):
            num_a = reports[i]
            num_b = reports[i + 1]

            if num_a < num_b:
                if not increasing:
                    line_safe = False
                    break
                diff = num_b - num_a
                if diff < 1 or diff > 3:
                    line_safe = False
                    break
            elif num_a > num_b:
                if increasing:
                    line_safe = False
                    break
                diff = num_a - num_b
                if diff < 1 or diff > 3:
                    line_safe = False
                    break
            else:
                line_safe = False
                break

        if line_safe:
            safe += 1

print(safe)
