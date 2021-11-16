import re

raw = input()

#a)
def decompression(s):
    bef, a, b, rest = re.match(r"(.*?)\((\d*)x(\d*)\)(.*)", s).groups()

    l = len(bef) + int(a) * int(b)
    if rest[int(a):] != "":
        l += decompression(rest[int(a):])

    return l


print(decompression(raw))

#b)
def real_decompr(s):
    try:
        bef, a, b, rest = re.match(r"(.*?)\((\d*)x(\d*)\)(.*)", s).groups()
    except:
        return len(s)

    l = len(bef)

    l += int(b) * real_decompr(rest[:int(a)])

    if rest[int(a):] != "":
        l += real_decompr(rest[int(a):])

    return l

print(real_decompr(raw))
