def opcodes(case, reg, a, b):
    #addr(reg, a, b):
    if case == 0:
        return reg[a] + reg[b]
    #addi(reg, a, b):
    elif case == 1:
        return reg[a] + b
    #mulr(reg, a, b):
    elif case == 2:
        return reg[a] * reg[b]
    #muli(reg, a, b):
    elif case == 3:
        return reg[a] * b
    #banr(reg, a, b):
    elif case == 4:
        return reg[a] & reg[b]
    #bani(reg, a, b):
    elif case == 5:
        return reg[a] & b
    #borr(reg, a, b):
    elif case == 6:
        return reg[a] | reg[b]
    #bori(reg, a, b):
    elif case == 7:
        return reg[a] | b
    #setr(reg, a, b):
    elif case == 8:
        return reg[a]
    #seti(reg, a, b):
    elif case == 9:
        return a
    #gtir(reg, a, b):
    elif case == 10:
        return (1 if a > reg[b] else 0)
    #gtri(reg, a, b):
    elif case == 11:
        return (1 if reg[a] > b else 0)
    #gtrr(reg, a, b):
    elif case == 12:
        return (1 if reg[a] > reg[b] else 0)
    #eqir(reg, a, b):
    elif case == 13:
        return (1 if a == reg[b] else 0)
    #eqri(reg, a, b):
    elif case == 14:
        return (1 if reg[a] == b else 0)
    #eqrr(reg, a, b):
    elif case == 15:
        return (1 if reg[a] == reg[b] else 0)

partOne = 592
print("a: " + str(partOne))


# part b)
opCodeValues = {}
for i in range(16):
    opCodeValues[i] = set([j for j in range(16)])

while True:
    try:
        bef = list(map(int, input().split("[")[1][:-1].split(",")))
        i, a, b, c = map(int, input().split())
        aft = list(map(int, input().split("[")[1][:-1].split(",")))

        toRemove = []
        for j in opCodeValues[i]:
            if aft[c] != opcodes(j, bef, a, b):
                toRemove.append(j)
                
        for j in toRemove:
            opCodeValues[i].remove(j)
        
        if len(opCodeValues[i]) == 1:
            (el, ) = opCodeValues[i]
            for j in range(16):
                if j != i:
                    opCodeValues[j].discard(el)
        input()

    except IndexError:
        input()
        registers = [0, 0, 0, 0]
        while True:
            try:
                i, a, b, c = map(int, input().split())
                (i, ) = opCodeValues[i]

                registers[c] = opcodes(
                    i,
                    registers,
                    a,
                    b
                )

            except:
                break
        
        break

solB = registers[0]
print("b: " + str(solB))
