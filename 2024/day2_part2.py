safe = 0

def is_safe(reports):
    if reports[0] < reports[1]:
        increasing = True
    elif reports[0] > reports[1]:
        increasing = False
    else:
        return False

    for i in range(len(reports) - 1):
        num_a = reports[i]
        num_b = reports[i + 1]

        if num_a < num_b:
            if not increasing:
                return False
            diff = num_b - num_a
            if diff < 1 or diff > 3:
                return False
        elif num_a > num_b:
            if increasing:
                return False
            diff = num_a - num_b
            if diff < 1 or diff > 3:
                return False
        else:
            return False

    return True

with open('2.txt') as f:
    lines = f.readlines()
    for line in lines:
        reports = list(map(int, line.split()))

        is_safe_ret = is_safe(reports)
        if is_safe_ret:
            safe += 1
        else:
            for j in range(len(reports)):
                new_reports = reports.copy()
                del new_reports[j]
                is_safe_ret = is_safe(new_reports)
                if is_safe_ret:
                    safe += 1
                    break

print(safe)
