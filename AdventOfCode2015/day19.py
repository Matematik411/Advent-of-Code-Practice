from queue import Queue
zdravilo = input()
menjave = {}
obrati = {}

while True:
    try:
        line = input().split()
    except:
        break

    levi = line[0]
    desni = line[2]

    if levi in menjave:
        menjave[levi].append(desni)
    else:
        menjave[levi] = [desni]

    if desni in obrati:
        obrati[desni].append(levi)
    else:
        obrati[desni] = [levi]

#part 1

print(menjave)
print(obrati)

def variacije(molekula, pravila, koliko):
    vse_mozne = set()
    max_d = max([len(x) for x in pravila])


    for i in range(len(molekula)):
        for l in range(min(max_d, len(molekula)-i)):
            orig = molekula[i:i+l+1]
            if orig in pravila:
                for pravilo in pravila[orig]:
                    nova = molekula[:i] + pravilo + molekula[i+l+1:]

                    vse_mozne.add(nova)
    
    vse_mozne = list(vse_mozne)
    vse_mozne.sort(reverse=True)
    vse_mozne.sort(key=lambda s: len(s))
    
    if koliko > 0:
        return vse_mozne[:koliko]
    else:
        return vse_mozne


print(len(variacije(zdravilo, menjave, -1)))

#part 2

aktivne = Queue()
aktivne.put((zdravilo, 0))
ze_narejene = set()

while not aktivne.empty():
    # print(aktivne)
    trenutna, koraki = aktivne.get()

    if trenutna == "e":
        print(trenutna, koraki)
        break  

    # if len(trenutna) == 1:
    #    continue

    # if trenutna in ze_narejene:
    #     continue

    # ze_narejene.add(trenutna)
    moznosti = variacije(trenutna, obrati, 1)
    #print(trenutna, moznosti, koraki)


    for primer in moznosti:
        if primer not in ze_narejene:
            aktivne.put((primer, koraki+1))
            ze_narejene.add(primer)





