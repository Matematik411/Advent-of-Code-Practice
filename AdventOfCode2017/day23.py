from collections import defaultdict
import sys
file = sys.stdin.read()

rules = [r.split() for r in file.split("\n")]
R = len(rules)

# changed for b)

registers = defaultdict(lambda: 0)
registers["a"] = 1

pos = 0

def value_of(a):
    try:
        return int(a)
    except:
        return registers[a]


mul_invoked = 0

while 0 <= pos < R:
    r, *d = rules[pos]

    if r == "set":
        x, y = d
        registers[x] = value_of(y)
    elif r == "sub":
        x, y = d
        registers[x] -= value_of(y)
    elif r == "mul":
        x, y = d
        registers[x] *= value_of(y)
        mul_invoked += 1
    elif r == "jnz":
        x, y = d
        if value_of(x) != 0:
            pos += value_of(y) - 1

    pos += 1
    # print(registers)

print("a: ", mul_invoked)


# b)

def prime(n):
    for k in range(2, n//2):
        if n % k == 0:
            return False
    return True


h = 0
for i in range(109900, 126901, 17):
    if not prime(i):
        h += 1

print("b: ", h)

