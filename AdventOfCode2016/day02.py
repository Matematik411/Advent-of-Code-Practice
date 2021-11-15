code = []
loc = 5

#b)
code2 = []
loc2 = 5

for _ in range(5):
    moves = input()
    for x in moves:
        if x == "U" and loc > 3:
            loc -= 3
        elif x == "L" and ((loc % 3) in {0, 2}):
            loc -= 1
        elif x == "D" and loc < 7:
            loc += 3
        elif x == "R" and (loc % 3 > 0):
            loc += 1
    
    for x in moves:
        if x == "U" and (loc2 not in {1, 2, 4, 5, 9}):
            if loc2 in {3, 13}:
                loc2 -= 2
            else:
                loc2 -= 4
        if x == "L" and (loc2 not in {1, 2, 5, 10, 13}):
            loc2 -= 1
        if x == "D" and (loc2 not in {5, 9, 10, 12, 13}):
            if loc2 in {1, 11}:
                loc2 += 2
            else:
                loc2 += 4
        if x == "R" and (loc2 not in {1, 4, 9, 12, 13}):
            loc2 += 1
    
    
    code.append(loc)
    code2.append(loc2)


print(code)
print(code2)
