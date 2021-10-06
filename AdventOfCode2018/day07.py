tree = {}
req = {}
reqB = {}
hasIn = set()

while True:
    try:
        line = input()
    except:
        break

    line = line.split(" must be finished before step ")
    a, b = line[0][-1], line[1][0]

    if a in tree:
        tree[a].append(b)
    else:
        tree[a] = [b]
    if b not in tree:
        tree[b] = []
    
    if b in req:
        req[b].append(a)
        reqB[b].append(a)
    else:
        req[b] = [a]
        reqB[b] = [a]
    
    hasIn.add(b)

pq = sorted(list(set(tree.keys()).difference(hasIn)))



word = ""

while pq:
    c = pq.pop(0)
    word += c

    for n in tree[c]:
        req[n].remove(c)

        if req[n] == []:
            pq.append(n)
            pq.sort()

print("a: "+ word)
print(len(word))
#b) --------------------
import string
values = dict()
for index, letter in enumerate(string.ascii_uppercase):
   values[letter] = index + 1

time = 0
tasks = [None for _ in range(5)]
pq = sorted(list(set(tree.keys()).difference(hasIn)))
wordB = ""

while len(wordB) < 26:
    for i in range(5):
        if tasks[i] == None and pq != []:
            new = pq.pop(0)
            timeReq = values[new] + 60

            tasks[i] = [new, timeReq]
    
    time += 1

    for i in range(5):
        if tasks[i] != None:
            if tasks[i][1] > 1:
                tasks[i][1] -= 1
            else:
                c = tasks[i][0]
                tasks[i] = None
                wordB += c

                for n in tree[c]:
                    reqB[n].remove(c)

                    if reqB[n] == []:
                        pq.append(n)
                        pq.sort()
    print(time, tasks, wordB)
    
print("b: " + wordB + " - time: " + str(time))


