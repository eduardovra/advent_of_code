
first_column = []
second_column = []

with open('1.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        numbers = line.split()
        first_column.append(int(numbers[0]))
        second_column.append(int(numbers[1]))

similarity_list = []

for i, number in enumerate(first_column):
    similarity_list.append(number * second_column.count(number))

print(sum(similarity_list))
