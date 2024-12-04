
first_column = []
second_column = []

with open('1.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        numbers = line.split()
        first_column.append(int(numbers[0]))
        second_column.append(int(numbers[1]))

first_column.sort()
second_column.sort()

differences = [abs(first_column[i] - second_column[i]) for i in range(len(first_column))]
print(sum(differences))
