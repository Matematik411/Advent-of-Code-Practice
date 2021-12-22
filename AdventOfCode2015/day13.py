import itertools

pocutja = {}
imena = set()

while True:
    try:
        line = input().split()
    except:
        break

    a = line[0]
    b = line[-1][:-1]
    x = int(line[3])
    if line[2] == "lose":
        x = -x

    pocutja[(a, b)] = x

    imena.add(a)
    imena.add(b)

imena = list(imena)
d = len(imena)

najboljse = 0
postavitev = None

for primer in itertools.permutations(imena):

    vsota = 0
    for i in range(d):
        srednji = primer[i]
        sosed1 = primer[(i+1) % d]
        sosed2 = primer[(i-1) % d]
        vsota += pocutja[(srednji, sosed1)]
        vsota += pocutja[(srednji, sosed2)]
    
    if vsota > najboljse:
        najboljse = vsota
        postavitev = primer

print(najboljse)
print(postavitev)

