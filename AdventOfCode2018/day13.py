board = []
carts = []
cardsCoords = set()
y = 0
# 0>    1<  2^  3v
while True:
    try:
        line = input()
    except EOFError:
        break

    i = line.find(">")
    while i >= 0:
        carts.append([y, i, 0, 0, 0])
        cardsCoords.add((y, i))
        line = line[:i] + "-" + line[i+1:]
        i = line.find(">")
    
    i = line.find("<")
    while i >= 0:
        carts.append([y, i, 1, 0, 0])
        cardsCoords.add((y, i))
        line = line[:i] + "-" + line[i+1:]
        i = line.find("<")
    
    i = line.find("^")
    while i >= 0:
        carts.append([y, i, 2, 0, 0])
        cardsCoords.add((y, i))
        line = line[:i] + "|" + line[i+1:]
        i = line.find("^")
    
    i = line.find("v")
    while i >= 0:
        carts.append([y, i, 3, 0, 0])
        cardsCoords.add((y, i))
        line = line[:i] + "|" + line[i+1:]
        i = line.find("v")

    board.append(line)
    y += 1




slash = {0: 2, 1: 3, 2: 0, 3: 1}
backSlash = {0: 3, 1: 2, 2: 1, 3: 0}
intersection = {(0, 0): 2, (1, 0): 3, (2, 0): 1, (3, 0): 0,
    (0, 1): 0, (1, 1): 1, (2, 1): 2, (3, 1): 3,
    (0, 2): 3, (1, 2): 2, (2, 2): 0, (3, 2): 1}
crash = False
round = 1

#b)
alive = len(carts)
while alive > 1:
    carts.sort()

    for i in range(len(carts)):
        y, x, d, c, a = carts[i]
        if a == 1:
            continue

        if d == 0:
            new = (y, x+1)
        elif d == 1:
            new = (y, x-1)
        elif d == 2:
            new = (y-1, x)
        else:
            new = (y+1, x)
        
        cardsCoords.remove((y, x))
        if new in cardsCoords:
            a = 1
            for j in range(len(carts)):
                yy, xx, dd, cc, aa = carts[j]
                if (yy, xx) == new and aa == 0:
                    carts[j] = [yy, xx, dd, cc, 1]
                    cardsCoords.remove(new)
                    alive -= 2
                    break
        else:
            cardsCoords.add(new)

        if board[new[0]][new[1]] == "/":
            d = slash[d]
        elif board[new[0]][new[1]] == "\\":
            d = backSlash[d]

        elif board[new[0]][new[1]] == "+":
            d = intersection[(d, c)]
            c += 1
            if c == 3:
                c = 0
        
        carts[i] = [new[0], new[1], d, c, a]

    round += 1

print([(c[1], c[0]) for c in carts if c[4] == 0][0])
