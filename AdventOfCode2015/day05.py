napake = ["ab", "cd", "pq", "xy"]

def preveri(niz):
    samoglasniki = 0
    naslednik = False
    
    for i in range(len(niz)-1):
        znak = niz[i]
        znak_nasl = niz[i+1]

        if znak in "aeiou":
            samoglasniki += 1
        
        if znak == znak_nasl:
            naslednik = True

        if (znak + znak_nasl) in napake:
            return False
    
    if niz[-1] in "aeiou":
        samoglasniki += 1

    return (samoglasniki >= 3) and (naslednik)

def preveri2(niz):
    trojke = False

    for i in range(len(niz)-2):
        znak = niz[i]
        znak_nasl = niz[i+2]
        
        if znak == znak_nasl:
            trojke = True

    dvojni_par = False
    pari = []

    for i in range(len(niz) - 1):
        par = niz[i:i+2]

        if (par in pari[:-1]):
            dvojni_par = True
        
        pari.append(par)

    return trojke and dvojni_par

lepe = 0
lepe2 = 0

while True:
    try:
        niz = input()
    except:
        break

    if preveri(niz):
        lepe += 1
    
    if preveri2(niz):
        lepe2 += 1

print(lepe)
print(lepe2)



