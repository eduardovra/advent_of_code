rules = []
numbers = []

with open('5.txt') as f:
    lines = f.readlines()
    reading_rules = True
    for line in lines:
        line = line.strip()
        if line == '':
            reading_rules = False
            continue
        if reading_rules:
            rule = line.split('|')
            rules.append((int(rule[0]), int(rule[1])))
        else:
            numbers.append([int(x) for x in line.split(',')])

print(rules)
print(numbers)

valid_numbers = []

for number_list in numbers:
    valid = True
    for r_1, r_2 in rules:
        if r_1 in number_list and r_2 in number_list:
            pos_r1 = number_list.index(r_1)
            pos_r2 = number_list.index(r_2)
            if pos_r1 > pos_r2:
                valid = False
                break
    if valid:
        valid_numbers.append(number_list)

total = 0
for number_list in valid_numbers:
    middle_number = number_list[len(number_list) // 2]
    total += middle_number

print(valid_numbers)
print(total)
