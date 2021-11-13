world = []
world.append(
    [0 for _ in range(52)]
)

for _ in range(50):
    line = input()
    world.append(
        [0] + [x for x in line] + [0]
    )
world.append(
    [0 for _ in range(52)]
)

print(len(world))
print(len(world[0]))



neigh_dirs = [(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)]

for year in range(1000): # this works for the solustion because of cycles in patterns
    new_world = [
        [0 for _ in range(52)] for _ in range(52)
    ]
    for x in range(1, 51):
        for y in range(1, 51):
            neighbors = [
                world[y + d[1]][x + d[0]] for d in neigh_dirs
            ]

            if world[y][x] == ".":
                NofTrees = neighbors.count("|")
                if NofTrees >= 3:
                    new_world[y][x] = "|"
                else:
                    new_world[y][x] = "."
            elif world[y][x] == "|":
                NofLumbers = neighbors.count("#")
                if NofLumbers >= 3:
                    new_world[y][x] = "#"
                else:
                    new_world[y][x] = "|"
            else:
                NofLumbers = neighbors.count("#")
                NofTrees = neighbors.count("|")
                if NofLumbers >= 1 and NofTrees >= 1:
                    new_world[y][x] = "#"
                else:
                    new_world[y][x] = "."

    world = new_world

    if year % 10 == 0:
        picture = ""
        for i in range(52):
            picture += "".join(map(str, new_world[i]))
        print(picture)

counters = [0, 0]
for line in world:
    counters[0] += line.count("|")
    counters[1] += line.count("#")
print(counters[0] * counters[1])