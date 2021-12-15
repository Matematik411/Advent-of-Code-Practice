podatki = input()
# podatki = r'[3, 2, {"a: 3, "g":2, "r":4, "e":"red"}]'

# [120,169,"green","red","orange"] -> 289
def prestej_seznam(niz):
    vsota = 0
    trenutni = 0
    minus = False

    for x in niz:
        if x == "-":
            minus = True
            continue

        try:
            x = int(x)
            trenutni = 10*trenutni + x

        except:
            if minus:
                vsota -= trenutni
            else:
                vsota += trenutni
            trenutni = 0
            minus = False

    return vsota

# {"e":59,"a":"yellow","d":"green","c":47, "g":"red"} -> 0
def prestej_slovar(niz):
    if "red" in niz:
        return 0
    
    return prestej_seznam(niz)


i = 0
oklepaji = []

while i < len(podatki):
    x = podatki[i]

    if x in "[{":
        oklepaji.append(i)
        i += 1

    elif x in "]}":
        zacetek = oklepaji.pop()
        if x == "]":
            racun = prestej_seznam(podatki[zacetek:i+1])
        else:
            racun = prestej_slovar(podatki[zacetek:i+1])

        podatki = podatki[:zacetek] + str(racun) + podatki[i+1:]
        i = zacetek
        if i == 0:
            print(podatki)
    else:
        i += 1
    