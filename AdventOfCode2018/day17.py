import re
def nice_print(t):
    s = ""
    for l in t:
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

clay[0][500-xmin] = "o"
alive = [(0, 500-xmin)]

for i in range(46423):
# while len(alive) > 0:

    print(len(alive))
    if i > 46420:
        nice_print(clay)
        print(len(alive))
        #print(alive)
    j, i = alive.pop()

    if j + 1 == h:
        continue
    if clay[j+1][i] == "o" and clay[j][i+1] in "o#" and clay[j][i-1] in "o#":
        continue

    if clay[j+1][i] in "#o":
        trapped = True
        #to left and right
        for k in [-1, 1]:
            if clay[j][i+k] in "o#":
                continue

            d = 0
            while True:
                d += k
                if clay[j][i+d] in ".o" and clay[j+1][i+d-k] in "#o":
                    clay[j][i+d] = "o"
                elif clay[j+1][i+d] == ".":

                    alive.append((j, i+d-k))
                    trapped = False
                    break
                else:
                    break
        if trapped:
            clay[j-1][i] = "o"
            alive.append((j-1, i))


    else:
        clay[j+1][i] = "o"
        alive.append((j+1, i))

nice_print(clay)
print(sum([x.count("o") for x in clay]))