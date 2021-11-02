import re
clay = []

while True:
    try:
        line = input()
    except:
        break

    a, b, c = map(int,re.match(r".=(\d*), .=(\d*)..(\d*)", line).groups())
    if line[0] == "x":
        clay.append((a, a, b, c))
    else:
        clay.append((b, c, a, a))
print("xmin")
print(min([data[0] for data in clay]))
print("xmax")
print(max([data[1] for data in clay]))
print("ymin")
print(min([data[2] for data in clay]))
print("ymax")
print(max([data[3] for data in clay]))
