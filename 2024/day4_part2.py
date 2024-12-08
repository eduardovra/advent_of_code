count = 0

with open("4.txt") as f:
    matrix = [l.strip() for l in f.readlines()]

    # M.S
    # .A.
    # M.S
    offsets = (
        {"M": ((-1, -1), (1, -1)), "S": ((-1, 1), (1, 1))},
        {"M": ((-1, 1), (1, 1)), "S": ((-1, -1), (1, -1))},
        {"M": ((-1, -1), (-1, 1)), "S": ((1, -1), (1, 1))},
        {"M": ((1, -1), (1, 1)), "S": ((-1, -1), (-1, 1))},
    )

    output = []
    for row in range(len(matrix)):
        output.append(["."] * len(matrix[row]))

    def find(letter, row, col):
        for offset in offsets:
            for pos in offset[letter]:
                r = row + pos[0]
                c = col + pos[1]
                if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[row]):
                    break
                if matrix[r][c] != letter:
                    break
            else:
                return True
        return False

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "A":
                # try to find M and S in the correct positions
                for offset in offsets:  # patterns
                    for letter, positions in offset.items(): # each 
                        if not find(letter, row, col):
                            break
                    else:
                        # found a pattern
                        count += 1
                        for letter, positions in offset.items():
                            for pos in positions:
                                r = row + pos[0]
                                c = col + pos[1]
                                output[r][c] = letter

                        break

for i, out in enumerate(output):
    print("".join(out))

print(count)
