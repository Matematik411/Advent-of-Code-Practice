import functools
data = list(map(int, input().split()))

tree = {}



def read(i, n):
    tree[n] = [None for _ in range(4)]
    tree[n][0] = data[i]
    tree[n][1] = data[i+1]
    tree[n][2] = []

    size = 2
    children = 0
    for j in range(tree[n][0]):
        children += 1
        tree[n][2].append(n + children)
        s, c = read(i + size, n  + children)

        size += s
        children += c
    
    tree[n][3] = data[i + size : i + size + tree[n][1]]
    size += tree[n][1]

    return size, children

#builds tree
read(0, 0)

solA = sum([sum(unit[3]) for unit in tree.values()])
print("a: " + str(solA))

#b) part

@functools.lru_cache(maxsize=None)
def value(node):
    info = tree[node]

    if info[0] == 0:
        return sum(info[3])

    else:
        this = 0
        for n in info[3]:
            if 0 < n < info[0] + 1:
                this += value(info[2][n-1])

        return this

print("b: " + str(value(0)))




