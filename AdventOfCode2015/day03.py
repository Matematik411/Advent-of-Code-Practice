navodila = input()

zeObiskano = {(0, 0)}
trenutno = [0, 0]
drugoTrenutno = [0, 0]
oseba = 0

smeri = ["^", ">", "<", "v"]
spremembe = [(0, 1), (1, 0), (-1, 0), (0, -1)]
spremembeX = [0, 1, -1, 0]
spremembeY = [1, 0, 0, -1]

for znak in navodila:
    kateri = smeri.index(znak)

    if oseba == 0:
        kateri = smeri.index(znak)
        trenutno = [trenutno[0] + spremembeX[kateri], trenutno[1] + spremembeY[kateri]]
        vnos = tuple(trenutno)
    else:
        kateri = smeri.index(znak)
        drugoTrenutno[0] += spremembeX[kateri]
        drugoTrenutno[1] += spremembeY[kateri]
        vnos = tuple(drugoTrenutno)

    if vnos not in zeObiskano:
        zeObiskano.add(vnos)

    oseba = 1 - oseba
    

aSol = 2081
print("a: " + str(aSol))
print("b: " + str(len(zeObiskano)))
