import re

plane = [[0 for _ in range(1000)] for _ in range(1000)]
cases = {}


while True:
    try:
        line = input()
    except:
        break

    id, x, y, w, h = map(int,re.match(r"#(\d*) @ (\d*),(\d*): (\d*)x(\d*)", line).groups())


    cases[(x, y)] = (w, h, id)
    for i in range(w):
        for j in range(h):
            plane[x + i][y + j] += 1
    

print("a: " + str(sum([sum([1 for x in plane[j] if x > 1]) for j in range(1000)])))
    
for (x, y), (w, h, id) in cases.items():
    covered = False

    for i in range(w):
        for j in range(h):
            if plane[x + i][y + j] != 1:
                covered = True
    
    if not covered:
        print("b: " + str(id))
        break