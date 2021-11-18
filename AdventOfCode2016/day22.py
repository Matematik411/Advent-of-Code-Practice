import re

nodes = {}
input()
input()
while True:
    try:
        line = input()
    except:
        break

    x, y, s, u, a = map(int, re.match(
        r"/dev/grid/node-x(\d*)-y(\d*)\s*(\d*)T\s*(\d*)T\s*(\d*)T.*", line).groups())

    nodes[(x, y)] = [s, u, a]

# #part a)
# data = [[v[2], v[1], k] for (k, v) in nodes.items()]
# data.sort(key = lambda x: x[1])
# print(data)
# viable = 0
# for (a, b, c) in data[:-1]:
#     i = 0
#     while b <= data[i][0]:
#         if c != data[i] and b != 0:
#             viable += 1
#         i += 1
# print(viable)
#viable = 1007, vsi razen 500+

data = [[v[2], v[1], k] for (k, v) in nodes.items() if k[1] == 0]
data.sort(key = lambda x: x[2][0])
print(data, len(data))


#x20-36
#y0-26
s = ""
for y in range(27):
    for x in range(37):
        if nodes[(x, y)][1] == 0:
            s += "_"
        elif nodes[(x, y)][0] >= 500:
            s += "#"
        else:
            s += "."
    s += "\n"
print(s)

# torej prazna (to je _ na (22, 25)) mora do (35, 0) --- AMPAK MORA okrog stene, torej najprej do (8, 4), nato do (35, 0)
# za to potrebuje (14 + 21) + (27 + 4)
# nato se rabi iskani data (tj (36, 0)) premakniti na (0, 0)
# za to rabi 35 premikov za eno polje, nato pa še enkrat le data levo: 35*5 + 1