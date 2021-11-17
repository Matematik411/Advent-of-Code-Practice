data = "10111100110001111"
size = 272 #solution a: 11100110111101110
size = 35651584

def extend(a, disk):
    while len(a) < disk:
        b = a[::-1]
        b = b.replace("0", "2")
        b = b.replace("1", "0")
        b = b.replace("2", "1")
        a = a + "0" + b
    return a

def checksum(s):
    sol = ""
    while len(sol) % 2 == 0:
        sol = ""
        for i in range(len(s) // 2):
            a, b = s[2*i : 2*i+2]
            if a == b:
                sol += "1"
            else:
                sol += "0"
        s = sol
    return sol

data = extend(data, size)
cs = checksum(data[:size])

print(cs)