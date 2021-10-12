scores = [3, 7]
size = 2
inputValue = 30121

code = [0, 0, 0, 0, 0, 0]

first = 0
second = 1

aEnd = False
bEnd = False
while not (aEnd and bEnd):
    scoreSum = scores[first] + scores[second]
    if scoreSum > 9:
        scores.append(scoreSum // 10)
        size += 1
        code = code[1:] + [scoreSum // 10]
        if sum([code[i] * (10 ** (5-i)) for i in range(6)]) - inputValue == 0:
            bSol = size - 6
            bEnd = True
    scores.append(scoreSum % 10)
    size += 1
    code = code[1:] + [scoreSum % 10]
    if sum([code[i] * (10 ** (5-i)) for i in range(6)]) - inputValue == 0:
        bSol = size - 6
        bEnd = True

    first = (first + scores[first] + 1) % size
    second = (second + scores[second] + 1) % size

    if size > inputValue + 10:
        aEnd = True

print("a: " + str(scores[inputValue : inputValue + 10]))
print("b: " + str(bSol))