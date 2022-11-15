import math
input_nr = 265149


# corners down right are 1 - 3**2 - 5**2 - 7**2 - ...

circle = math.ceil(math.sqrt(input_nr))
if circle % 2 == 0:
    circle += 1

corner = circle * circle

difference = corner - input_nr
# it is in the bottom edge

distance = circle // 2 + (circle // 2 - difference)

print("a: ", distance)

# b)
grid = [[0 for _ in range(301)] for _ in range(301)]
neigh = [(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)]

move = [(0, 1), (-1, 0), (0, -1), (1, 0)]

# 1xR 1xU - 2xL 2xD - 3xR 3xU - 4xL 4xD - 5xR ...

pos = [150, 150]
grid[pos[0]][pos[1]] = 1

direction = 0
repetition = [1, 0]
reps_done = 0

while True:
    pos[0] += move[direction][0]
    pos[1] += move[direction][1]
    reps_done += 1
    if reps_done == repetition[0]:
        repetition[1] += 1
        if repetition[1] == 2:
            repetition = [repetition[0] + 1, 0]
        direction = (direction + 1) % 4
        reps_done = 0
    
    value = sum([grid[pos[0] + n[0]][pos[1] + n[1]] for n in neigh])
    grid[pos[0]][pos[1]] = value


    if value > input_nr:
        print("b: ", value)
        break

