registers = [12, 0, 0, 0]
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

    if case[0] == "mult":
        registers[0] += registers[1] * registers[3]
        registers[2] = 0
        registers[3] = 0
        i += 5

    elif case[0] == "cpy":
        if case[2] not in "abcd":
            pass
        elif case[1] in "abcd":
            registers[names[case[2]]] = registers[names[case[1]]]
        else:
            registers[names[case[2]]] = int(case[1])
    
    elif case[0] == "inc":
        if case[1] not in "abcd":
            pass
        else:
            registers[names[case[1]]] += 1

    elif case[0] == "dec":
        registers[names[case[1]]] -= 1
    
    elif case[0] == "jnz":
        if case[1] in "abcd":
            if registers[names[case[1]]] != 0:
                i += int(case[2]) - 1
        else:
            if int(case[1]) != 0:
                if case[2] in "abcd":
                    i += registers[names[case[2]]] - 1
                else:
                    i += int(case[2]) - 1
    
    else:
        if case[1] in "abcd":
            j = i + registers[names[case[1]]]
        else:
            j = i + int(case[1])
        
        if j < len(instr):
            old = instr[j]

            if old[0] == "cpy":
                instr[j] = ["jnz", old[1], old[2]]
            elif old[0] == "jnz":
                instr[j] = ["cpy", old[1], old[2]]
            elif old[0] in ["dec", "tgl"]:
                instr[j] = ["inc", old[1]]
            else:
                instr[j] = ["dec", old[1]]
            
    i += 1
    #print(instr)


#a = 12860
print(registers)


