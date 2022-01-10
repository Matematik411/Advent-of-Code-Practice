real = {
"children": 3,
"cats": 7,
"samoyeds": 2,
"pomeranians": 3,
"akitas": 0,
"vizslas": 0,
"goldfish": 5,
"trees": 3,
"cars": 2,
"perfumes": 1
}


def preveri(data):

    for kljuc in data:
        if kljuc in ["cats", "trees"]:
            if data[kljuc] <= real[kljuc]:
                return False

        elif kljuc in ["pomeranians", "goldfish"]:
            if data[kljuc] >= real[kljuc]:
                return False

        else:
            if data[kljuc] != real[kljuc]:
                return False
    
    return True

while True:
    try:
        line = input().split()
    except:
        break

    prvi = line[2][:-1]
    prvi_vred = int(line[3][:-1])   
    drugi = line[4][:-1]
    drugi_vred = int(line[5][:-1])
    tretji = line[6][:-1]
    tretji_vred = int(line[7])

    trenutni = {prvi: prvi_vred, drugi: drugi_vred, tretji: tretji_vred}

    if preveri(trenutni):
        print(line[1][:-1])