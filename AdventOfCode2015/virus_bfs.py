import sys
import math
from queue import Queue
from collections import defaultdict

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
g = [[] for i in range(n)]
exits = []
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    g[n1].append(n2)
    g[n2].append(n1)
for i in range(e):
    ei = int(input())  # the index of a gateway node
    exits.append(ei)
# game loop

def to_cut(s, t):

    paths = []

    visited = set()
    q = Queue()
    #(current, distance, 1st neigh)
    q.put((s, 0, -1))
    while not q.empty():
        c, d , fst = q.get()
        if c in visited:
            continue
        
        visited.add(c)

        for neigh in g[c]:
            if neigh == t:
                if fst < 0:
                    paths.append((s, neigh, d+1))
                else:
                    paths.append((s, fst, d+1))
            
            if neigh not in visited:
                if fst < 0:
                    q.put((neigh, d+1, neigh))
                else:
                    q.put((neigh, d+1, fst))
    
    return paths




while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn

    done = set()
    appeared = defaultdict(lambda: 0)
    pos = []
    doubles = defaultdict(set)


    closest = [0, 0]
    closest_d = n

    for e in exits:
        pths = to_cut(e, si)
        for (x1, x2, d) in pths:
            if (x1, x2) not in done:
                appeared[x2] += 1
                doubles[x2].add(x1)
                done.add((x1, x2))
                pos.append((x1, x2, d))
    print(pos, done, doubles)
    if min([ds[2] for ds in pos]) < 2:
        print("aaaaaaaaaaa", min([ds[2] for ds in pos]))
        new = [x for x in pos if x[2] == min([ds[2] for ds in pos])]
    else:
        new = [x for x in pos if len(doubles[x[1]]) > 1]
    # print(new)
    new.sort(key = lambda x : x[2])
    new.sort(key = lambda x : -appeared[x[1]])
    # print(new)
    closest = new[0][:2]
    # print(closest)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    g[closest[0]].remove(closest[1])
    g[closest[1]].remove(closest[0])

    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    print(" ".join(map(str, closest)))
