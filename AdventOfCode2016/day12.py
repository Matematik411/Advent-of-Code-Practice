registers = [0, 0, 1, 0]
names = {"a": 0, "b": 1, "c": 2, "d": 3}
instr = []

while True:
    try:
        line = input().split()
    except:
        break

    instr.append(line)

i = 0
while i < len(instr):
    case = instr[i]

    if case[0] == "cpy":
        if case[1] in "abcd":
            registers[names[case[2]]] = registers[names[case[1]]]
        else:
            registers[names[case[2]]] = int(case[1])
    
    elif case[0] == "inc":
        registers[names[case[1]]] += 1

    elif case[0] == "dec":
        registers[names[case[1]]] -= 1
    
    else:
        if case[1] in "abcd":
            if registers[names[case[1]]] != 0:
                i += int(case[2]) - 1
        else:
            if int(case[1]) != 0:
                i += int(case[2]) - 1


    i += 1

#a) 318083
print(registers)


