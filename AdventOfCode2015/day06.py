import re
grid = [[0 for _ in range(1000)] for _ in range(1000)]

def toggle(a, b, c, d):
    for x in range(a, c+1):
        for y in range(b, d+1):
            grid[y][x] += 2
    
def turn(a, b, c, d, way):
    for x in range(a, c+1):
        for y in range(b, d+1):
            grid[y][x] = max(grid[y][x] + way, 0)

while True:
    try:
        line = input()
    except:
        break

    instr, a, b, c, d = re.match(r"(.*) (\d*),(\d*) through (\d*),(\d*)", line).groups()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)

    if instr == "toggle":
        toggle(a, b, c, d)
    elif instr[-2:] == "on":
        turn(a, b, c, d, 1)
    else:
        turn(a, b, c, d, -1)

print("solution a: ", 569999)
print("solution b: ", sum([sum(vrstica) for vrstica in grid]))
