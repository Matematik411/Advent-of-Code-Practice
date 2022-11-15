import sys
file = sys.stdin.read()

instructions = [int(line) for line in file.split()]
size = len(instructions)

pos = 0
steps = 0

while 0 <= pos < size:
    move = instructions[pos]
    instructions[pos] += 1
    pos += move
    steps += 1

print("a: ", steps)

instructions_b = [int(line) for line in file.split()]


pos = 0
steps = 0

while 0 <= pos < size:
    move = instructions_b[pos]
    if move >= 3:
        instructions_b[pos] -= 1
    else:
        instructions_b[pos] += 1
        
    pos += move
    steps += 1

print("b: ", steps)

