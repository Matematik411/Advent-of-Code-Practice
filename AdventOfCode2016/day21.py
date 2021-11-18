import re
password = [x for x in "abcdefgh"]
code = [x for x in "fbgdceah"]
#code = [x for x in "decab"]

def swap(pwd, i, j):
    pwd[i], pwd[j] = pwd[j], pwd[i]
    return pwd

def swap_letter(pwd, a, b):
    for i in range(len(pwd)):
        if pwd[i] == a:
            pwd[i] = b
        elif pwd[i] == b:
            pwd[i] = a
    return pwd

def rotate(pwd, side, a=False, n=1):
    if n == 0:
        return pwd
    if a:
        i = pwd.index(a)
        if i >= 4:
            return rotate(pwd, side, n=i+2)
        else:
            return rotate(pwd, side, n=i+1)
    elif side:
        pwd = rotate(pwd, side, n=n-1)
        return [pwd[-1]] + pwd[:-1]
    else:
        pwd = rotate(pwd, side, n=n-1)
        return pwd[1:] + [pwd[0]]

def rotate_b(pwd, a):
    pwd = rotate(pwd, False)
    k = 0
    while pwd.index(a) != k:
        pwd = rotate(pwd, False)
        if k == 3:
            pwd = rotate(pwd, False)
        k += 1
    return pwd

def reverse(pwd, i, j):
    for k in range((j-i+1)//2):
        pwd[i+k], pwd[j-k] = pwd[j-k], pwd[i+k]
    return pwd

def move(pwd, i, j):
    if i > j:
        pwd = pwd[:j] + rotate(pwd[j:i+1], True) + pwd[i+1:]
    else:
        pwd = pwd[:i] + rotate(pwd[i:j+1], False) + pwd[j+1:]
    return pwd

orders = []
while True:
    try:
        line = input()
        orders.append(line)
    except:
        break

#part a)
for line in orders:
    if line[:13] == "swap position":
        a, b = map(int, re.match(r"swap position (\d*) with position (\d*)", line).groups())
        password = swap(password, a, b)
    elif line[:11] == "swap letter":
        x, y = re.match(r"swap letter (.) with letter (.)", line).groups()
        password = swap_letter(password, x, y)
    elif line[:17] == "reverse positions":
        i, j = map(int, re.match(r"reverse positions (\d*) through (\d*)", line).groups())
        password = reverse(password, i, j)
    elif line[:13] == "move position":
        i, j = map(int, re.match(r"move position (\d*) to position (\d*)", line).groups())
        password = move(password, i, j)
    elif line[:6] == "rotate" and line[-2] != " ":
        x, y = re.match(r"rotate (.*) (\d*) .*", line).groups()
        password = rotate(password, x == "right", n=int(y))
    else:
        (x,) = re.match(r".* letter (.)", line).groups()
        password = rotate(password, True, x)  
print("".join(password))

#part b)
for line in orders[::-1]:
    if line[:13] == "swap position":
        a, b = map(int, re.match(r"swap position (\d*) with position (\d*)", line).groups())
        code = swap(code, a, b)
    elif line[:11] == "swap letter":
        x, y = re.match(r"swap letter (.) with letter (.)", line).groups()
        code = swap_letter(code, x, y)
    elif line[:17] == "reverse positions":
        i, j = map(int, re.match(r"reverse positions (\d*) through (\d*)", line).groups())
        code = reverse(code, i, j)
    elif line[:13] == "move position":
        i, j = map(int, re.match(r"move position (\d*) to position (\d*)", line).groups())
        code = move(code, j, i)
    elif line[:6] == "rotate" and line[-2] != " ":
        x, y = re.match(r"rotate (.*) (\d*) .*", line).groups()
        code = rotate(code, x == "left", n=int(y))
    else:
        (x,) = re.match(r".* letter (.)", line).groups()
        code = rotate_b(code, x)
    
print("".join(code))

