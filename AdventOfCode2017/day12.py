# 2000 programs

graph = {i : [] for i in range(2000)}

for node in range(2000):
    info = input().split()[2:]

    for neigh in info:
        neigh = int(neigh.replace(",", ""))
        graph[node].append(neigh)

# we do bfs to see which ones we can reach from 0
groups = []
already_in_group = set()
starting = 0

while starting < 2000:
    visited = set()
    stack = [starting]

    while stack:
        c = stack.pop()

        if c in visited:
            continue

        visited.add(c)

        for n in graph[c]:
            if n not in visited:
                stack.append(n)
    
    groups.append(visited)
    already_in_group = already_in_group.union(visited)

    starting += 1
    while starting in already_in_group:
        starting += 1

print("a: ", len(groups[0]))
print("b: ", len(groups))