#name, id, checksum = re.match(r"(.*)-(\d*)\[(.....)\]", line).groups()

import re

screen = [["." for _ in range(50)] for _ in range(6)]
def nice_print(s):
    p = ""
    for l in screen:
        p += "".join(l) + "\n"
    print(p)
nice_print(screen)

while True:
    try:
        line = input()
    except:
        break

    if "rect" == line[:4]:
        a, b = map(int, re.match(r"rect (\d*)x(\d*)", line).groups())
        
        for i in range(a):
            for j in range(b):
                screen[j][i] = "#"
    
    else:
        d, a, b = re.match(r".*(.)=(\d*) by (\d*)", line).groups()
        a = int(a)
        b = int(b)

        if d == "y":
            new = ["." for _ in range(50)]

            for i in range(50):
                new[(i + b) % 50] = screen[a][i]
        
            screen[a] = new
        else:
            new = ["." for _ in range(6)]

            for i in range(6):
                new[(i + b) % 6] = screen[i][a]
            
            for i in range(6):
                screen[i][a] = new[i]
    
    nice_print(screen)

print(sum([x.count("#") for x in screen]))