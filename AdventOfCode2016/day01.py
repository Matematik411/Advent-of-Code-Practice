instructions = input().split(", ")
pos = 0
dirs = {0: 1j,  1: 1, 2: -1j, 3: -1}
dir = 0

for x in instructions:
    if x[0] == "R":
        dir += 1
    else:
        dir -= 1
    dir %= 4
    pos += dirs[dir] * int(x[1:])

print(abs(pos.real) + abs(pos.imag))

#b)
pos = 0
dir = 0
visited = {0}
found = False

for x in instructions:
    if x[0] == "R":
        dir += 1
    else:
        dir -= 1
    dir %= 4
    
    for i in range(int(x[1:])):
        pos += dirs[dir]
        if pos in visited:
            print(abs(pos.real) + abs(pos.imag))
            found = True
            break
        visited.add(pos)
    
    if found:
        break