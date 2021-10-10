plants = input()[15:]
input()

yes = set()
no = set()
for _ in range(32):
    line = input().split(" => ")

    if line[1] == ".":
        no.add(line[0])
    else:
        yes.add(line[0])

move = -3
plants = [".", ".", "."] + [x for x in plants] + [".", ".", "."]

aPart = 20
highest = 95 # calculated before
diff = 32
prev = 0

for r in range(1, 10000):
    if plants[2] == "#":
        plants = ["."] + plants
        move -= 1
    if plants[-3] == "#":
        plants += "."
    
    d = len(plants)
    new = ["." for _ in range(d)]

    here = ["."] + plants[:4]
    for i in range(2, d-2):
        here = here[1:] + [plants[i + 2]]
        if "".join(here) in yes:
            new[i] = "#"
    
    plants = new
    value = sum([i + move for i in range(len(plants)) if plants[i] == "#"])

    if value - prev != diff:
        highest = r
    prev = value

    if r == highest:
        atHighest = value
    if r == aPart:
        print("a: " + str(value))
 
print(atHighest)
bResult = atHighest + (50000000000 - highest) * diff
print("b: " + str(bResult))
