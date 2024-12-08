import re

with open('3.txt') as f:
    data = f.readlines()
    matches = re.findall(r'mul\((\d+),(\d+)\)', ''.join(data))
    result = 0
    for match in matches:
        result += int(match[0]) * int(match[1])
    print(result)
