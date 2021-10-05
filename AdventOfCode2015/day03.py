navodila = input()

zeObiskano = {(0, 0)}
trenutno = [0, 0]

for znak in navodila:
    if znak == "^":
        trenutno[1] += 1
        vnos = tuple(trenutno)
        if vnos not in zeObiskano:
            zeObiskano.add(vnos)

    elif znak == ">":
        trenutno[0] += 1
        vnos = tuple(trenutno)
        if vnos not in zeObiskano:
            zeObiskano.add(vnos)

    elif znak == "<":
        trenutno[0] -= 1
        vnos = tuple(trenutno)
        if vnos not in zeObiskano:
            zeObiskano.add(vnos)

    else:
        trenutno[1] -= 1
        vnos = tuple(trenutno)
        if vnos not in zeObiskano:
            zeObiskano.add(vnos)

print("a: " + str(len(zeObiskano)))