import hashlib
start_code = "pvhmgsws"
pict = "#########\n# | | | #\n#-#-#-#-#\n# | | | #\n#-#-#-#-#\n# | | | #\n#-#-#-#-#\n# | | |  \n####### V\n"

def nice_print(l):
    x, y = l
    i = 10 * (2*y+1) + 1 + 2*x
    nice = "\n" + "-" * 12 + "\n" + pict[:i] + "S" + pict[i+1:]
    print(nice)

def doors(s):
    return [s[i] in "bcdef" for i in range(4)]

dirs = "UDLR"
moves = [[0, -1], [0, 1], [-1, 0], [1, 0]]

loc = [0, 0]
path = ""

while True:
    if loc == [3, 3 ]:
        break

    nice_print(loc)
    print("Current path: ", path)
    full = start_code + path
    code = hashlib.md5(full.encode("utf-8")).hexdigest()

    open = doors(code)
    print("Open doors: ", ",".join([dirs[i] for i in range(4) if open[i]]))
    
    step = input("Choose a direction to move: ")
    valid = False
    while not valid:
        if step == "B":
            loc = [loc[0] - moves[dirs.index(path[-1])][0], loc[1] - moves[dirs.index(path[-1])][1]]
            path = path[:-1]
            valid = True
        elif step not in ["U", "D", "L", "R"]:
            print("You didn't write a valid direction!")
            step = input("Choose the direction again: ")
        else:
            new = [loc[0] + moves[dirs.index(step)][0], loc[1] + moves[dirs.index(step)][1]]
            if new[0] < 0 or new[1] < 0:
                print("You can't move outside the 4x4 grid!")
                step = input("Choose the direction again: ")
            else:
                loc = new
                path += step
                valid = True

print("You completed the maze! Congratulations! Your path was ", path)
#A: DRRDRLDURD