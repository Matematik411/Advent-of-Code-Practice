instructions = []
while True:
    try:
        line = input().replace(",", "").split()
    except:
        break

    instructions.append(line)

reg = {"a": 0, "b" : 0}

def operation(data):
    if data[0] == "hlf":
        reg[data[1]] //= 2

    elif data[0] == "tpl":
        reg[data[1]] *= 3

    elif data[0] == "inc":
        reg[data[1]] += 1
   
    elif data[0] == "jmp":
        return int(data[1])
    elif data[0] == "jie":
        if reg[data[1]] % 2 == 0:
            return int(data[2])
    elif data[0] == "jio":
        if reg[data[1]] == 1:
            return int(data[2])
    
    return 1



i = 0
while 0 <= i < len(instructions):
    i += operation(instructions[i])
    # the code does the following
    # if i == 40:
    #     res = 0
    #     a = reg["a"]
    #     while a > 1:
    #         res += 1
    #         if a %2 == 0:
    #             a //= 2
    #         else:
    #             a = 3*a + 1
    #     print(res)
    #     break

print(reg)