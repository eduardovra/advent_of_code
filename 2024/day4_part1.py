count = 0

with open('4.txt') as f:
    matrix = [l.strip() for l in f.readlines()]

    offsets = (
        ((0, 0), (0, 1), (0, 2), (0, 3)),
        ((0, 0), (0, -1), (0, -2), (0, -3)),
        ((0, 0), (1, 0), (2, 0), (3, 0)),
        ((0, 0), (-1, 0), (-2, 0), (-3, 0)),
        ((0, 0), (1, 1), (2, 2), (3, 3)),
        ((0, 0), (-1, -1), (-2, -2), (-3, -3)),
        ((0, 0), (1, -1), (2, -2), (3, -3)),
        ((0, 0), (-1, 1), (-2, 2), (-3, 3)),
    )

    def get_string(r, c, offset_idx):
        s = []

        for offset in offsets[offset_idx]:
            row = r+offset[0]
            col = c+offset[1]
            if row < 0 or col < 0:
                return None
            try:
                s.append(matrix[row][col])
            except IndexError:
                return None

        return ''.join(s)

    output = []
    for row in range(len(matrix)):
        output.append(['.'] * len(matrix[row]))

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            for i in range(len(offsets)):
                if get_string(row, col, i) == 'XMAS':
                    count += 1

                    for offset in offsets[i]:
                        r = row+offset[0]
                        c = col+offset[1]
                        output[r][c] = matrix[r][c]

for i, out in enumerate(output):
    print(''.join(out))

print(count)
