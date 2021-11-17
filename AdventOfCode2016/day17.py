import hashlib
start_code = "pvhmgsws"

def doors(s):
    return [s[i] in "bcdef" for i in range(4)]

dirs = "UDLR"
moves = [[0, -1], [0, 1], [-1, 0], [1, 0]]


stack = [[0, 0, ""]]
max_len = 0
sol = ""

while len(stack) > 0:
    x, y, path = stack.pop()

    if [x, y] == [3, 3]:
        if len(path) > max_len:
            max_len = len(path)
            sol = path
            print(max_len)
        continue

    full = start_code + path
    code = hashlib.md5(full.encode("utf-8")).hexdigest()

    open = doors(code)
    for i in range(4):
        if open[i]:
            new = [x + moves[i][0], y + moves[i][1]]
            if -1 < new[0] < 4 and -1 < new[1] < 4:
                stack.append([new[0], new[1], path + dirs[i]])

#A: DRRDRLDURD
print(sol, max_len)