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

print(f'{rules=}')
print(f'{numbers=}')

valid_numbers = []
invalid_numbers = []

for number_list in numbers:
    valid = True
    loop = True
    while loop:
        for r_1, r_2 in rules:
            if r_1 in number_list and r_2 in number_list:
                pos_r1 = number_list.index(r_1)
                pos_r2 = number_list.index(r_2)
                if pos_r1 > pos_r2:
                    valid = False
                    tmp = number_list[pos_r1]
                    number_list[pos_r1] = number_list[pos_r2]
                    number_list[pos_r2] = tmp
                    break
        else:
            loop = False
    if valid:
        valid_numbers.append(number_list)
    else:
        invalid_numbers.append(number_list)

total = 0
for number_list in invalid_numbers:
    middle_number = number_list[len(number_list) // 2]
    total += middle_number

print(f'{valid_numbers=}')
print(f'{invalid_numbers=}')
print(f'{total=}')
