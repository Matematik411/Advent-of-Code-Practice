stevec = 0

while True:
    try:
        znaki = input()
    except:
        break

    stevec += 4
    
    i = 1
    while i < len(znaki)-1:
        if znaki[i] == "\\":
            if znaki[i+1] == "x":
                stevec += 1
                i += 3
            else:
                stevec += 2
                i += 1
        i += 1

print("a: ", 1342)
print(stevec)