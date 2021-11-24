import itertools

razdalje = {}
mesta = set()

while True:
    try:
        line = input().split()
    except:
        break

    a = line[0]
    b = line[2]
    x = int(line[4])

    razdalje[(a, b)] = x

    mesta.add(a)
    mesta.add(b)

mesta = list(mesta)

najkrajsa_razd = 10000
dejanska_pot = None
najdaljsa_razd = -1

for primer in itertools.permutations(mesta):
    pot = 0

    for i in range(len(primer)-1):
        a = primer[i]
        b = primer[i+1]

        r = razdalje.get((a, b), -1)
        if r < 0:
            r = razdalje.get((b, a), -1)

        pot += r
    
    if pot < najkrajsa_razd:
        najkrajsa_razd = pot
        dejanska_pot = primer
    if pot > najdaljsa_razd:
        najdaljsa_razd = pot

print("najkrajsa razdalja po vseh sedmih je: ", najkrajsa_razd, "pot je bila: ", dejanska_pot)
print("najdaljsa razdalja po vseh sedmih je: ", najdaljsa_razd)

