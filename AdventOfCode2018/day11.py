serial = 1955

# GRID OF PARTIAL SUMS TO THAT POINT FROM POINT (0, 0)
grid = [[0 for _ in range(301)] for _ in range(301)]

for x in range(1, 301):
    for y in range(1, 301):
        power = (((((x + 10) * y) + serial) * (x + 10) % 1000) // 100) - 5
        grid[y][x] = power + grid[y][x-1] + grid[y-1][x] - grid[y-1][x-1]


# a)----------
totalA = 0
locA = [0, 0]
for x in range(1, 299):
    for y in range(1, 299):
        here = grid[y + 2][x + 2] - grid[y + 2][x - 1] - grid[y - 1][x + 2] + grid[y - 1][x - 1]

        if here > totalA:
            totalA = here
            locA = [x, y]

print("a: " + str(locA) + " with the sum of: " + str(totalA))

# b)----------
totalB = 0
locB = [0, 0, 0]
for x in range(1, 301):
    for y in range(1, 301):
        sizeM = 301 - max(x, y)
        for s in range(1, sizeM + 1):
            here = grid[y + s - 1][x + s - 1] - grid[y + s - 1][x - 1] - grid[y - 1][x + s - 1] + grid[y - 1][x - 1]

            if here > totalB:
                totalB = here
                locB = [x, y, s]

print("b: " + str(locB) + " with the sum of: " + str(totalB))
