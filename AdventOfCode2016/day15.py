s = 0

table = [False for _ in range(6)]

while not all(table):
    table = [False for _ in range(6)]

    if s + 1 + 15 % 17 == 0:
        table[0] = True
    
    if s + 2 + 2 % 3 == 0:
        table[1] = True
    
    if s + 3 + 4 % 19 == 0:
        table[2] = True
    
    if s + 4 + 2 % 13 == 0:
        table[3] = True
    
    if s + 5 + 2 % 7 == 0:
        table[4] = True
    
    if s + 6 + 0 % 5 == 0:
        table[5] = True
    
    print(s)
    s += 1

print(s-1)
