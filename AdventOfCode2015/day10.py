zac = "1113122113"

def look_and_say(s):
    nov = ""
    t = s[0]
    n = 0
    for x in s:
        if x == t:
            n += 1
        else:
            nov += str(n) + t
            t = x
            n = 1
    nov += str(n) + t

    return nov


for _ in range(50):
    zac = look_and_say(zac)

print(len(zac))