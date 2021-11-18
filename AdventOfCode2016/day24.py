from queue import Queue
import itertools

map = []
locations = {}
for j in range(41):
    line = input()
    map.append(line)
    for i in range(8):
        if line.find(str(i)) >= 0:
            locations[i] = (line.index(str(i)), j)
dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

dist = [[-1 for _ in range(8)] for _ in range(8)]
for i in range(8):
    dist[i][i] = 0
    for j in range(i):
        dist[i][j] = dist[j][i]
    found = i+1

    #BFS
    visited = {locations[i]}
    q = Queue()
    q.put([locations[i], 0])

    while found < 8:
        (x, y), d = q.get()

        for k in range(4):
            new_x, new_y = (x+dirs[k][0], y+dirs[k][1])
            if map[new_y][new_x] != "#" and (new_x, new_y) not in visited:
                q.put([(new_x, new_y), d+1])
                visited.add((new_x, new_y))
                if map[new_y][new_x] != ".":
                    n = int(map[new_y][new_x])
                    if dist[i][n] < 0:
                        dist[i][n] = d+1
                        found += 1

paths = itertools.permutations([i for i in range(1, 8)])

min_path = []
min_sol = 1000000
for path in paths:
    lenght = 0
    prev = 0
    for a in path:
        lenght += dist[prev][a]
        prev = a
    if lenght < min_sol:
        min_sol = lenght
        min_path = path

print(min_path, min_sol)

#b)
paths = itertools.permutations([i for i in range(1, 8)])
min_circle = []
circle_sol = 1000000
for path in paths:
    lenght = 0
    prev = 0
    for a in path:
        lenght += dist[prev][a]
        prev = a
    lenght += dist[prev][0]
    
    if lenght < circle_sol:
        circle_sol = lenght
        min_circle = path

print(min_circle, circle_sol)