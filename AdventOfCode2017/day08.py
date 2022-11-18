from collections import defaultdict

registers = defaultdict(lambda: 0)
max_value = 0

while True:
    try:
        line = input()
    except EOFError:
        break

    ins = line.split()

    ins[4] = "registers['" + ins[4] + "']"
    condition = " ".join(ins[4:])

    if eval(condition):
        value = int(ins[2]) if ins[1] == "inc" else -int(ins[2])
        registers[ins[0]] += value

    
    if registers[ins[0]] > max_value:
        max_value = registers[ins[0]]

print("a: ", max(registers.values()))
print("b: ", max_value)
