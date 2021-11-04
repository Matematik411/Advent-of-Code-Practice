import hashlib
koda = "ckczppom"
koda = "bgvyzdsv"

st = 0
while True:
    st += 1
    niz = koda + str(st)

    zakodirano = hashlib.md5(niz.encode("utf-8")).hexdigest()

    if zakodirano[:6] == "000000":
        print(st)
        break


