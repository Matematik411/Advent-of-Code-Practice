podatki = []
imena = []

while True:
    try:
        line = input().split()
    except:
        break

    sestavina = line[0][:-1]
    capacity = int(line[2][:-1])   
    durability = int(line[4][:-1])
    flavor = int(line[6][:-1])
    texture = int(line[8][:-1])
    calories = int(line[10])

    podatki.append([capacity, durability, flavor, texture, calories])
    imena.append(sestavina)

zlice = 100
najboljsi = 0
najboljsi_primer = None

for i in range(zlice+1):
    for j in range(zlice+1-i):
        for k in range(zlice+1-i-j):
            l = zlice-i-j-k

            cap = i * podatki[0][0] + j * podatki[1][0] + k * podatki[2][0] + l * podatki[3][0]
            cap = max(cap, 0)
            
            dur = i * podatki[0][1] + j * podatki[1][1] + k * podatki[2][1] + l * podatki[3][1]
            dur = max(dur, 0)

            fla = i * podatki[0][2] + j * podatki[1][2] + k * podatki[2][2] + l * podatki[3][2]
            fla = max(fla, 0)

            text = i * podatki[0][3] + j * podatki[1][3] + k * podatki[2][3] + l * podatki[3][3]
            text = max(text, 0)

            calo = i * podatki[0][4] + j * podatki[1][4] + k * podatki[2][4] + l * podatki[3][4]
            calo = max(calo, 0)

            vred = cap * dur * fla * text

            if vred > najboljsi and calo == 500:
                najboljsi = vred
                najboljsi_primer = (i, j, k, l)


print(najboljsi, najboljsi_primer)



