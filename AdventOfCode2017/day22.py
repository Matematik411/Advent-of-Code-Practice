import sys
from collections import defaultdict
file = sys.stdin.read().split("\n")
# input size is 25x25 so we start at [12][12]

grid = defaultdict(lambda: 3)

# b) states are 0 -> 3
# 0 .. weakened

for j, row in enumerate(file):
    for i, state in enumerate(row):
        grid[(j-12, i-12)] = 1 if state == "#" else 3

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

pos = (0, 0)
facing = 0

infects = 0

for burst in range(10000000):
    state = grid[pos]
    
    facing = (facing + state) % 4
    grid[pos] = (state + 1) % 4

    if state == 0:
        infects += 1

    pos = (
        pos[0] + directions[facing][0],
        pos[1] + directions[facing][1]
    )

print("a: ", 5266)
print("b: ", infects)
    
