grid = []

for _ in range(100):
    vrsta = [x for x in input()]
    grid.append(vrsta)

def posodobi(x, y):
    trenutno = grid[y][x]
    sosedi = 0

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            x_n = x + dx
            y_n = y + dy
            if (x, y) != (x_n, y_n):
                # print(dy, dx, "-------------", y, x)
                if 0 <= x_n <= 99 and 0 <= y_n <= 99:
                    if grid[y_n][x_n] == "#":
                        sosedi += 1


    if trenutno == "#":
        if sosedi in [2, 3]:
            return "#"
        else:
            return "."

    else:
        if sosedi == 3:
            return "#"
        else:
            return "."

def nice_print(mreza):
    picture = ""
    for l in mreza:
        picture += "".join(l) + "\n"
    print(picture)


for krog in range(100):
    nova = [["#" for _ in range(100)] for _ in range(100)]

    for x in range(100):
        for y in range(100):
            if (x, y) not in [(0, 0), (0, 99), (99, 0), (99, 99)]:
                nova[y][x] = posodobi(x, y)
    
    grid = nova

    nice_print(grid)

print(sum([vrsta.count("#") for vrsta in grid]))



