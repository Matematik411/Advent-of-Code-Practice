from functools import lru_cache

data = []
upper_nodes = set()
while True:
    try:
        line = input().replace(",", "")
    except EOFError:
        break
    line = line.split()
    line[1] = int(line[1][1:-1])

    data.append(line)

    for name in line[3:]:
        upper_nodes.add(name)

# a) we just need the bottom one

for node in data:
    if len(node) > 2:
        if node[0] not in upper_nodes:
            print("a: ", node[0])
            break
start_node = "gmcrj"

# b) something is unbalanced
@lru_cache(maxsize=None)
def subtrees_weights(name):
    root_node = [node for node in data if node[0] == name][0]

    if len(root_node) == 2:
        return [0]
    
    weights = []
    for subtree in root_node[3:]:
        other_node = [node for node in data if node[0] == subtree][0]
        weights.append(
            sum(subtrees_weights(subtree)) + other_node[1]
        )

    return weights

minimal = 1000000
problem = None
print("b: \n")
for node in data:
    subtrees = subtrees_weights(node[0])

    # check unbalanced
    # find the smallest value
    if not all(v == subtrees[0] for v in subtrees):

        if min(subtrees) < minimal:
            minimal = min(subtrees)
            problem = node

print(problem)
print(subtrees_weights(problem[0]))
print("too heavy - ", [node for node in data if node[0] == problem[4]][0])
print("mdbtyw : 396 -> 391 _____ so the answer for b is 5")
