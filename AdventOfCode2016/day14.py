import hashlib
salt = "ahsbgdzn"

code_indexi = []
i = 0
searching = []
while len(code_indexi) < 64:
    zakodirano = salt + str(i)
    for _ in range(2017):
        zakodirano = hashlib.md5(zakodirano.encode("utf-8")).hexdigest()

    if len(searching) > 0 and i - searching[0][0] > 1000:
        searching = searching[1:]

    end = False
    for (j, x) in searching:
        for k in range(len(zakodirano)-4):
            if zakodirano[k:k+5] == 5*x:
                code_indexi.append(j)
                end = True
                print(len(code_indexi))
                break

        

    triplet = ""
    for k in range(len(zakodirano)-2):
        a, b, c = zakodirano[k:k+3]
        if a == b == c:
            triplet = a + b + c
            break
    if triplet:
        searching.append((i, a))

    i += 1
    #print(code_indexi, len(code_indexi), i)

print("solution b: ", code_indexi[63])
print("solution a: ", 23890)
