# DOES NOT WORK - works too long, too much size...
line = input()[1:-1]

def process(data):
    curr = ""
    poss = []
    inner = []

    i = 0
    d = len(data)
    while i < d:
        x = data[i]
        if x in "NESW":
            if inner == []:
                curr += x
            else:
                for k in range(len(inner)):
                    inner[k] += x
            i += 1
        elif x == "|":
            if inner == []:
                poss.append(curr)
            else:
                poss.append(inner)
            curr = ""
            inner = []
            i += 1
        elif x == "(":
            level = 1
            j = i
            while level > 0:
                j += 1
                if data[j] == "(":
                    level += 1
                elif data[j] == ")":
                    level -= 1

            if inner == []:
                inner = process(data[i+1:j])
                for k in range(len(inner)):
                    inner[k] = curr + inner[k]
            else:
                inner_new = process(data[i+1:j])
                all_cases = []
                for case in inner:
                    for case_new in inner_new:
                        all_cases.append(case + case_new)
                
                inner = all_cases
            i = j + 1

    if inner == []:
        poss.append(curr)
    else:
        poss.append(inner)

    flattened = []
    for el in poss:
        if isinstance(el, list):
            for x in el:
                flattened.append(x)
        else:
            flattened.append(el)
    return flattened

#possibilities = process("N(W|)N(W|)N")
possibilities = process(line)
print(possibilities)

dirs = {"N": [0, 1], "E": [1, 0], "S": [0, -1], "W": [-1, 0]}
dirs_i = {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]}
new_room = {"N": [0, 0, 1, 0], "E": [0, 0, 0, 1], "S": [1, 0, 0, 0], "W": [0, 1, 0, 0]}

curr = [0, 0]
# [N, E, S, W]
rooms = {(0, 0): [[0, 0, 0, 0], 0]}

for path in possibilities:
    curr = [0, 0]

    for x in path:
        if x in "NESW":
            new = [
                curr[0] + dirs[x][0],
                curr[1] + dirs[x][1]
            ]

            tNew = tuple(new)
            if tNew not in rooms:
                rooms[tNew] = [new_room[x].copy(), 0]
            else:
                rooms[tNew][0][new_room[x].index(1)] = 1
            
            rooms[tuple(curr)][0][new_room[x].index(1)-2] = 1

            curr = new
#print(possibilities)
print(rooms)

#se BFS

from queue import Empty, Queue
q = Queue(maxsize=0)
visited = {(0, 0)}

q.put((0, 0))
while not q.empty():
    c = q.get()



    here = rooms[c]
    for i in range(4):
        if here[0][i] == 1:
            new = [
                c[0] + dirs_i[i][0],
                c[1] + dirs_i[i][1]
            ]
            new = tuple(new)
            if new not in visited:
                rooms[new][1] = here[1] + 1
                visited.add(new)
                q.put(new)

#print(rooms)
print(max([r[1] for r in rooms.values()]))



