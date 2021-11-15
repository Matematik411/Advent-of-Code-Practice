import hashlib
door_id = "ugkcyxxp"
password = ""

i = 0
while len(password) < 8:
    niz = door_id + str(i)

    zakodirano = hashlib.md5(niz.encode("utf-8")).hexdigest()

    if zakodirano[:5] == "00000":
        print(zakodirano, i)
        password += zakodirano[5]
    
    i += 1

print(password)

#b)
password_real = [False for _ in range(8)]

def nice_print(list):
    sol = ""
    for x in list:
        if x:
            sol += x
        else:
            sol += "_"
    return sol

i = 0
while not all(password_real):
    niz = door_id + str(i)
    zakodirano = hashlib.md5(niz.encode("utf-8")).hexdigest()

    if zakodirano[:5] == "00000":
        print("testing case: ", i, " old pass:", nice_print(password_real))
        try:
            if not password_real[int(zakodirano[5])]:
                password_real[int(zakodirano[5])] = zakodirano[6]
                print("password updated: ", nice_print(password_real))

        except:
            i += 1
            continue

    
    i += 1