def opcodes(case, reg, a, b):
    #addr(reg, a, b):
    if case == "addr":
        return reg[a] + reg[b]
    #addi(reg, a, b):
    elif case == "addi":
        return reg[a] + b
    #mulr(reg, a, b):
    elif case == "mulr":
        return reg[a] * reg[b]
    #muli(reg, a, b):
    elif case == "muli":
        return reg[a] * b
    #banr(reg, a, b):
    elif case == "banr":
        return reg[a] & reg[b]
    #bani(reg, a, b):
    elif case == "bani":
        return reg[a] & b
    #borr(reg, a, b):
    elif case == "borr":
        return reg[a] | reg[b]
    #bori(reg, a, b):
    elif case == "bori":
        return reg[a] | b
    #setr(reg, a, b):
    elif case == "setr":
        return reg[a]
    #seti(reg, a, b):
    elif case == "seti":
        return a
    #gtir(reg, a, b):
    elif case == "gtir":
        return (1 if a > reg[b] else 0)
    #gtri(reg, a, b):
    elif case == "gtri":
        return (1 if reg[a] > b else 0)
    #gtrr(reg, a, b):
    elif case == "gtrr":
        return (1 if reg[a] > reg[b] else 0)
    #eqir(reg, a, b):
    elif case == "eqir":
        return (1 if a == reg[b] else 0)
    #eqri(reg, a, b):
    elif case == "eqri":
        return (1 if reg[a] == b else 0)
    #eqrr(reg, a, b):
    elif case == "eqrr":
        return (1 if reg[a] == reg[b] else 0)

input()
ip = 0
special = 2

data = []
while True:
    try:
        line = input().split()
        data.append(line)
    except:
        break
print(data)
s = len(data)

register = [1, 0, 0, 0, 0, 0]
k = 0
while ip < s and k < 30:
    k += 1
    register[special] = ip

    instr = data[ip][0]
    a, b, c = map(int, data[ip][1:])

    sol = opcodes(instr, register, a, b)
    register[c] = sol

    ip = register[special] + 1
    print(register)
    
#part a: 1536
