# hex grid
# n-s +-1
# ne -0.5

#   \ n  /
# nw +--+ ne
#   /    \
# -+      +-
#   \    /
# sw +--+ se
#   / s  \

# n: +1, 0
# ne: +0.5, +1
# ...

moves = input().split(",")

change = {
    "n": (1, 0), "ne": (0.5, 1), "se": (-0.5, 1), "s": (-1, 0), "sw": (-0.5, -1), "nw": (0.5, -1)}

position = [0, 0]

max_distance = 0
# solution is +, + 
# ... quickest backing is SW * position[1] + S * (position[0] - 1/2 * position[1])
def dist(loc):
    return loc[1] + (loc[0] - loc[1] / 2)


for move in moves:
    position[0] += change[move][0]
    position[1] += change[move][1]

    away = dist(position)
    if away > max_distance:
        max_distance = away


print(position)
print("a: ", dist(position))
print("b: ", max_distance)