import re
def nice_print(t):
    s = ""
    for l in t[:200]:
        s += "".join(l[250:]) + "\n"
    print(s)

xmin = 108 - 1
w = 537-108+3
ymin = 3
h = 1913-3+1
clay = [["." for _ in range(w)] for _ in range(h)]
while True:
    try:
        line = input()
    except:
        break

    # (x1, y1, x2, y2)
    a, b, c = map(int,re.match(r".=(\d*), .=(\d*)..(\d*)", line).groups())
    if line[0] == "x": #vertical
        for i in range(b, c+1):
            clay[i-ymin][a-xmin] = "#"
    else: #horizontal
        for i in range(b, c+1):
            clay[a-ymin][i-xmin] = "#"


# clay = [". . . | . . .".split(),"# . . . . . #".split(), "# . # # # . #".split(), "# . # # # . #".split(), "# . . . . . #".split(), "# # # # # # #".split()]
# clay[0][3] = "|"
# alive.append((0, 3))
clay[0][500-xmin] = "|"
alive = []
alive.append((0, 500-xmin))

print("------------------------------------------ NNNNNNNNNNNEEEEEEEEEWWWWWWWWW_------------------")
while len(alive) > 0:
    nice_print(clay)

    j, i = alive[0]
    alive = alive[1:]
    # if j > 108:
    #     break

    # if clay[j+1][i] == "o" and clay[j][i+1] in "o#" and clay[j][i-1] in "o#":
    #     continue
    try:
        while clay[j+1][i] == ".":
            j = j+1
            clay[j][i] = "|"
    except:
        continue
    
    while True:
        to_colour = {(j, i)}
        trapped = True
        from_before = [False, False]
        #to left and right
        for k in [-1, 1]:
            d = 0
            while True:
                if clay[j][i+d+k] == "#":
                    z = 0
                    z_ch = 0
                    if k < 0 and from_before[1]:
                        z_ch = 1
                    elif k > 0 and from_before[0]:
                        z_ch = -1
                    if z_ch != 0:
                        spots_from_here = set()
                        while clay[j][i+z] == "|":
                            spots_from_here.add((j, i+z))
                            z += z_ch
                        if clay[j+1][i+z-z_ch] in ".|": #this a bit sketchy
                            trapped = False
                        else:
                            to_colour.update(spots_from_here)
                    break
                elif clay[j][i+d+k] == "." and clay[j+1][i+d] in "~#" and clay[j+1][i+d+k] in "~#":
                    to_colour.add((j,i+d+k))
                elif clay[j][i+d+k] == "|" and (j, i+d+k) not in alive:
                    to_colour.add((j,i+d+k))
                elif clay[j][i+d+k] == "|":
                    if k < 0:
                        from_before[0] = True
                    else:
                        from_before[1] = True
                    break
                else:
                    to_colour.add((j,i+d+k))
                    alive.append((j,i+d+k))
                    trapped = False
                    break
                d += k
        if trapped:
            for (y, x) in to_colour:
                clay[y][x] = "~"
            j -= 1
        else:
            for (y, x) in to_colour:
                clay[y][x] = "|"
            break



nice_print(clay)
print(sum([x.count("o") for x in clay]))