import re
dates = []

while True:
    try:
        line = input()
    except:
        break

    dates.append(re.match(r"\[(\d*).(\d*).(\d*) (\d*):(\d*)\] (.*)", line).groups())
dates.sort()

sleeping = {}

for case in dates:
    if case[5][0] == "G":
        id = int(re.findall(r"Guard #(.*) begins shift", case[5])[0])
        
        if id not in sleeping:
            sleeping[id] = [0 for _ in range(60)]
        
        current = sleeping[id]
    
    elif case[5][0] == "f":
        start = int(case[4])
    
    else:
        end = int(case[4])

        for i in range(start, end):
            current[i] += 1

# a.....
sleepy = -1
sleepHours = 0
for p, l in sleeping.items():
    if sum(l) > sleepHours:
        sleepHours = sum(l)
        sleepy = p

mostMinute = -1
mostSleeps = 0
for i in range(60):
    if sleeping[sleepy][i] > mostSleeps:
        mostSleeps = sleeping[sleepy][i]
        mostMinute = i

print("a: " + str(sleepy * mostMinute))

# b.....
pathTwo = (-1, -1)
mostSleeps = 0
for p, l in sleeping.items():
    for i in range(60):
        if l[i] > mostSleeps:
            mostSleeps = l[i]
            pathTwo = (p, i)

print("b: " + str(pathTwo[0] * pathTwo[1]))