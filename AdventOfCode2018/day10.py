import re
coords = []
for line in open('inputs\input10.txt'):
    x, y, dx, dy = map(int, re.findall('-?\d+', line))
    coords.append([x, y, dx, dy])

minDist = 200000000
tBest = 0
coordsBest = None
for t in range(20000):
    xmin, xmax, ymin, ymax = 50000, -50000, 50000, -50000

    for (x, y, dx, dy) in coords:
        if x + dx * t < xmin:
            xmin = x + dx * t 

        if x + dx * t > xmax:
            xmax = x + dx * t

        if y + dy * t < ymin:
            ymin = y + dy * t 
        
        if y + dy * t > ymax:
            ymax = y + dy * t 
    
    if xmax - xmin + ymax - ymin < minDist:
        tBest = t
        minDist = xmax - xmin + ymax - ymin
        coordsBest = [xmin, xmax, ymin, ymax]

xmin, xmax, ymin, ymax = coordsBest
locations = [["." for _ in range(xmax - xmin + 3)] for _ in range(ymax - ymin + 3)]

for (x, y, dx, dy) in coords:
    xRel = (x + tBest * dx) - xmin + 1
    yRel = (y + tBest * dy) - ymin + 1

    locations[yRel][xRel] = "#"

writing = ""
for line in locations:
    writing += "".join(line) + "\n"

print(tBest, coordsBest)
print(writing)

