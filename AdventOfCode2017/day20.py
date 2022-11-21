import re
import sys
from collections import defaultdict
file = sys.stdin.read()

search_q = r'p=<(.*)>, v=<(.*)>, a=<(.*)>'

points = [[list(map(int, x.split(","))) for x in p] for p in re.findall(search_q, file)]

# a)
# we find the smallest acc

def size(v):
    res = 0
    for a in v:
        res += abs(a)
    return res

closest = 0
min_acc = size(points[0][2])

for i, p in enumerate(points):
    acc_size = size(p[2])

    if acc_size < min_acc:
        min_acc = acc_size
        closest = i

print("a: ", closest)

# b) we actually simulate

for round in range(100):

    locations = defaultdict(lambda: [])

    for i, p in enumerate(points):
        
        for axis in range(3):
            p[1][axis] += p[2][axis]
            p[0][axis] += p[1][axis]
        
        locations[tuple(p[0])].append(i)

    deleted = []
    for (k, v) in locations.items():
        if len(v) > 1:
            for p_i in v:
                deleted.append(p_i)

    deleted.sort(key= lambda x: -x)

    if deleted:
        for i in deleted:
            del points[i]

print("b: ", len(points))


