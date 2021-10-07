n = 425
m = 7084800
SPEC = 23

scores = [0 for _ in range(n)]
player = 0
current = 0
nghbrs = {0: [0, 0]}

for i in range(1, m + 1):
    player += 1
    if player == n:
        player = 0
    
    if i % SPEC == 0:
        scores[player] += i

        r = current
        for _ in range(7):
            r = nghbrs[r][0]
        
        current = nghbrs[r][1]
        scores[player] += r

        nghbrs[nghbrs[r][0]][1] = nghbrs[r][1]
        nghbrs[nghbrs[r][1]][0] = nghbrs[r][0]

    
    else:
        counterClock = nghbrs[current][1]
        Clock = nghbrs[counterClock][1]

        nghbrs[i] = [counterClock, Clock]
        nghbrs[counterClock][1] = i
        nghbrs[Clock][0] = i

        current = i

print("a: " + str(max(scores)))
