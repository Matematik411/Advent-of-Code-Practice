import re

instr = {}
starting = []

#outputs are negative - 1
operatives = {}
queue = []

while True:
    try:
        line = input()
    except:
        break

    if line[:3] == "bot":
        a, x, b, y, c = re.match(r"bot (\d*) gives low to (.*) (\d*) and high to (.*) (\d*)", line).groups()

        instr[int(a)] = [
            int(b) if x == "bot" else -int(b)-1,
            int(c) if y == "bot" else -int(c)-1
        ]
    else:
        a, b = re.match(r"value (\d*) goes to bot (\d*)", line).groups()

        starting.append([int(a), int(b)])

#initial instructions
for (a, b) in starting:
    if b in operatives:
        operatives[b].append(a)
        queue.append(b)
    else:
        operatives[b] = [a] 

#moving around
while len(queue) > 0:
    bot = queue.pop()
    if bot < 0:
        continue

    values = operatives.pop(bot)
    values.sort()

    if values == [17, 61]:
        print("solution a: ", bot)

    for i in range(2):
        a = values[i]
        b = instr[bot][i]

        if b in operatives:
            operatives[b].append(a)
            queue.append(b)
        else:
            operatives[b] = [a] 

print("done")
print("solution b: ", operatives[-1][0] * operatives[-2][0] * operatives[-3][0])
