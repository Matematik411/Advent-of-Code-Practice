from functools import lru_cache
from queue import PriorityQueue

depth = 4080
target = (14, 785)
# depth = 510
# target = (10, 10)

@lru_cache(maxsize=None)
def erosion_level(loc):
    x, y = loc
    if (x, y) in [(0, 0), target]:
        ind = 0
    elif y == 0:
        ind = x * 16807
    elif x == 0:
        ind = y * 7905
    else:
        ind = erosion_level((x-1, y)) * erosion_level((x, y-1)) 
    level = (ind + depth) % 20183
    return level
print("risk level for a) is: ", 11843)

risk_level = 0
ww, hh = 30, 840
grid = [[0 for _ in range(ww)] for _ in range(hh)]
for i in range(ww):
    for j in range(hh):
        grid[j][i] = erosion_level((i, j)) % 3

grid = [[-1] + row + [-1] for row in grid]
grid = [[-1 for _ in range(ww+2)]] + grid + [[-1 for _ in range(ww+2)]]
    

dirs = {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]}
#eqp: 0 ... nothing ||| 1 ... torch ||| 2 ... climbing

def time_req(a, b, eq):
    if b < 0:
        p = []
    elif a == 0:
        if eq == 1:
            if b == 0:
                p = [(1, 1), (8, 2)]
            elif b == 1:
                p = [(8, 2)]
            else:
                p = [(1, 1)]
        elif eq == 2:
            if b == 0:
                p = [(8, 1), (1, 2)]
            elif b == 1:
                p = [(1, 2)]
            else:
                p = [(8, 1)]
    elif a == 1:
        if eq == 0:
            if b == 0:
                p = [(8, 2)]
            elif b == 1:
                p = [(1, 0), (8, 2)]
            else:
                p = [(1, 0)]
        elif eq == 2:
            if b == 0:
                p = [(1, 2)]
            elif b == 1:
                p = [(8, 0), (1, 2)]
            else:
                p = [(8, 0)]
    else:
        if eq == 0:
            if b == 0:
                p = [(8, 1)]
            elif b == 1:
                p = [(1, 0)]
            else:
                p = [(1, 0), (8, 1)]
        elif eq == 1:
            if b == 0:
                p = [(1, 1)]
            elif b == 1:
                p = [(8, 0)]
            else:
                p = [(8, 0), (1, 1)]
    return p

visited = set()
pq = PriorityQueue()
pq.put((0, 1, (1, 1)))

while not pq.empty():
    t, e, (x, y) = pq.get()

    if (x, y, e) in visited:
        continue

    if (x-1, y-1) == target:
        if e == 1:
            print("time to get to target is: ", t)
            break
        else:
            print("here, no thorch", t)

    visited.add((x, y, e))

    for i in range(4):
        x_n = x + dirs[i][0]
        y_n = y + dirs[i][1]
        possible = time_req(grid[y][x], grid[y_n][x_n], e)
        for (dt, e_n) in possible:
            if ((x_n, y_n, e_n) not in visited):
                pq.put((t + dt, e_n, (x_n, y_n)))
