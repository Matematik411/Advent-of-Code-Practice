import string
d = dict(zip(string.ascii_lowercase, range(26)))
de = dict(zip(range(26), string.ascii_lowercase))

def preveri(niz):
    trojke = False

    for i in range(len(niz)-2):
        a, b, c = niz[i:i+3]
      
        if (d[b] - d[a] == 1) and (d[c] - d[b] == 1):
            trojke = True

    for i in range(len(niz)):
        znak = niz[i]
        if znak in "iol":
            return False

    dvojni_par = 0
    pari = []

    for i in range(len(niz) - 1):
        par = niz[i:i+2]

        if (par[0] == par[1]):
            if par[0] not in pari:
                dvojni_par += 1
            pari.append(par[0])
        
    return trojke and (dvojni_par >= 2)

geslo = "hxbxwxba"

def naslednje(s):
    i = -1
    nova_vrednost = 0

    while (nova_vrednost % 26) == 0:
        znak = s[i]
        vrednost = d[znak]
        nova_vrednost = vrednost + 1
        nov = de[nova_vrednost % 26]
        s_n = s[:i] + nov
        if i < -1:
            s_n += s[i+1:]
        s = s_n
        i -= 1

    return s

nova_najdena = 0
while nova_najdena < 2:
    geslo = naslednje(geslo)

    if preveri(geslo):
        print("novo geslo je: ", geslo)
        nova_najdena += 1

