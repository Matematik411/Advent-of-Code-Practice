original = input()

polymer = original

def react(poly):
    i = 1
    while True:
        try:
            if poly[i].upper() == poly[i-1].upper() and poly[i] != poly[i-1]:
                poly = poly[:i-1] + poly[i+1:]
                if i > 0:
                    i -= 1
            else:
                i += 1
        except:
            break

    return(poly)


print("a: " + str(len(react(polymer))))


tried = set()
minLenght = len(original)
minLetter = None

for x in original:
    if x.upper() not in tried:
        tried.add(x.upper())
        polymer = original
        polymer = polymer.replace(x.upper(), "")
        polymer = polymer.replace(x.lower(), "")
        polymer = react(polymer)

        if len(polymer) < minLenght:
            minLenght = len(polymer)
            minLetter = x.upper()

print("b: " + str(minLenght) + " (" + minLetter + ")")



