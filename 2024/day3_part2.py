import re

with open('3.txt') as f:
    data = f.readlines()
    matches = re.findall(r'(mul\((\d+),(\d+)\)|do\(\)|don\'t\(\))', ''.join(data))
    #print(matches)
    #exit()
    result = 0
    do = True
    for match in matches:
        if match[0] == 'do()':
            do = True
        elif match[0] == 'don\'t()':
            do = False
        elif do:
            result += int(match[1]) * int(match[2])
    print(result)
