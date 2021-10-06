coords = []
while True:
    try:
        pair = list(map(int, input().split(",")))
        coords.append(pair)
    except:
        break

xmin = min([pair[0] for pair in coords])
xmax = max([pair[0] for pair in coords])
ymin = min([pair[1] for pair in coords])
ymax = max([pair[1] for pair in coords])

xd = xmax - xmin + 3
yd = ymax - ymin + 3

board = [[(-1, xmax + ymax) for _ in range(xd)] for _ in range(yd)]

def update(i, a, b):
    for xRel in range(xd):
        for yRel in range(yd):
            x = xmin - 1 + xRel
            y = ymin - 1 + yRel
            d = abs(a-x) + abs(b-y)

            if d < board[yRel][xRel][1]:
                board[yRel][xRel] = (i, d)
            elif d == board[yRel][xRel][1]:
                board[yRel][xRel] = (-1, d)

for (j, (x, y)) in enumerate(coords):
    update(j, x, y)

infinite = set([i[0] for i in board[0]])
infinite = infinite.union(set([i[0] for i in board[yd-1]]))
infinite = infinite.union(set([i[0][0] for i in board]))
infinite = infinite.union(set([i[xd-1][0] for i in board]))


biggest = -1
pos = 0
for i in range(len(coords)):
    area = sum([[pair[0] for pair in board[j]].count(i) for j in range(yd)])
    if (area > biggest) and (i not in infinite):
        biggest = area
        pos = i

print("a: " + str(biggest) + " (" + str(pos) + ")")

# b) --- 
upperB = 10000
count = 0

for xRel in range(xd):
    for yRel in range(yd):
        x = xmin - 1 + xRel
        y = ymin - 1 + yRel

        sumDist = sum([abs(x - pair[0]) + abs(y - pair[1]) for pair in coords])

        if sumDist < upperB:
            count += 1

print("b: " + str(count))
