from queue import Queue
floors = [
#t: [E THG THM PLG PLM STG STM PRG PRM RUG RUM]
    [0 for _ in range(11)],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0]
]

def is_safe(l):
    has_gen = False
    has_uncon_micro = False

    for i in range(5):
        if l[2*i + 2] - l[2*i + 1] > 0:
            has_uncon_micro = True
        if l[2*i + 1] > 0:
            has_gen = True

    return not (has_gen and has_uncon_micro)

def new_plan(plan, e, i, d):
    new = []

    for j in range(4):
        f = [x for x in plan[j]]
        if j == e:
            f[i] = 0
            f[0] = 0
        elif j == e+d:
            f[i] = 1
            f[0] = 1
        new.append(f)
    
    return new


dist = {}
dist[str(floors)] = 0
q = Queue()
q.put([floors, 0])

while not q.empty():
    building, k = q.get()

    if sum(building[0]) == 11:
        print("solution a: ", k)
        break

    e = [i for i in range(4) if building[i][0] == 1][0]

    #ena stvar v dvigalu
    for i in range(1, 11):
        if building[e][i] > 0:

            if e > 0:
                after_move = new_plan(building, e, i, -1)
                if str(after_move) not in dist:
                    if is_safe(after_move[e-1]) and is_safe(after_move[e]):
                        q.put([after_move, k+1])
                        dist[str(after_move)] = k+1
            
            if e < 3:
                after_move = new_plan(building, e, i, 1)
                if str(after_move) not in dist:
                    if is_safe(after_move[e+1]) and is_safe(after_move[e]):
                        q.put([after_move, k+1])
                        dist[str(after_move)] = k+1

    #dve stvari v dvigalu
    for i in range(1, 11):
        for j in range(i+1, 11):
            if (building[e][i] + building[e][j] == 2) and ((i % 2 == j % 2) or (abs(i-j) == 1 and i % 2 == 1)):
                if e > 0:
                    after_move = new_plan(building, e, i, -1)
                    after_move = new_plan(after_move, e, j, -1)
                    if str(after_move) not in dist:
                        if is_safe(after_move[e-1]) and is_safe(after_move[e]):
                            q.put([after_move, k+1])
                            dist[str(after_move)] = k+1
                
                if e < 3:
                    after_move = new_plan(building, e, i, 1)
                    after_move = new_plan(after_move, e, i, 1)
                    if str(after_move) not in dist:
                        if is_safe(after_move[e+1]) and is_safe(after_move[e]):
                            q.put([after_move, k+1])
                            dist[str(after_move)] = k+1
                




    
