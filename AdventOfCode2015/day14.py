podatki = {}

while True:
    try:
        line = input().split()
    except:
        break

    ime = line[0]
    hitrost = int(line[3])   
    cas = int(line[6])
    pocitek = int(line[-2])

    podatki[ime] = [hitrost, cas, pocitek]


def razdalja(ime, t):
    # a, b, c = [1, 2, 3]
    v, t_0, t_1 = podatki[ime]

    pot = (t // (t_0 + t_1)) * v * t_0

    pot += min(t_0, t % (t_0 + t_1)) * v

    return pot


cas_dirke = 2503
najdaljse = 0
zmagovalec = None
for ime in podatki:
    pot = razdalja(ime, cas_dirke)
    if pot > najdaljse:
        najdaljse = pot
        zmagovalec = ime
print("prvi del: ")
print(zmagovalec, najdaljse)

# --------------------------------------------------------------------


imena = [ime for ime in podatki]
tocke = [0 for _ in podatki]
razdalje = [0 for _ in podatki]
stanje = [podatki[ime][1] for ime in podatki]

for cas in range(2503):

    for i in range(len(imena)):
        ime = imena[i]
        smer = stanje[i]
        if stanje[i] > 0:
            razdalje[i] += podatki[ime][0]
            stanje[i] -= 1
        else:
            stanje[i] += 1

        if stanje[i] == 0:
            if smer == 1:
                stanje[i] = -podatki[ime][2]
            else:
                stanje[i] = podatki[ime][1]
    
    prvi = max(razdalje)
    for i in range(len(imena)):
        if razdalje[i] == prvi:
            tocke[i] += 1

print("drugi del")
print(imena[tocke.index(max(tocke))], max(tocke))






