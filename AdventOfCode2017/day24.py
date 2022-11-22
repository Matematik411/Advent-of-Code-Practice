import sys
file = sys.stdin.read().split("\n")

parts = [tuple(map(int, l.split("/"))) for l in file]
parts.sort()

# greedy doesn't work : 1044

complete = []
possible = [[{(0, 30)}, 30]]



while possible:
    path, c = possible.pop()

    there_is_next = False
    for pair in parts:
        if c in pair and pair not in path:
            a, b = pair
            new = path.union({pair})
            if a == c:
                next = b
            else:
                next = a
            possible.append([new, next])
            there_is_next = True

    if not there_is_next:
        complete.append(path)
    
sum_over_all = 0
        
max_sum = 0
max_length = 0
for path in complete:
    s = 0
    for fst, snd in path:
        s += fst + snd
    
    # a) 
    if s > sum_over_all:
        sum_over_all = s
    # b)
    if len(path) >= max_length:
        if len(path) > max_length:
            max_length = len(path)
            max_sum = s
        
        elif s > max_sum:
            max_sum = s

print("a: ", sum_over_all)
print("b: ", max_sum)

