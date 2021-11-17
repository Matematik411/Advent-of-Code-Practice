m = [17, 3, 19, 13, 7, 5, 11]
M = 17*3*19*13*7*5*11
z = [M//17, M//3, M//19, M//13, M//7, M//5, M//11]

a = [1, 2, 12, 7, 0, 4, 4]

def inv_mod(x, mod):
    x %= mod
    o = x

    k = 1
    while x != 1:
        x = (x + o) % mod
        k += 1
    
    return k

y = [inv_mod(z[i], m[i]) for i in range(7)]
w = [y[i] * z[i] % M for i in range(7)]

x = sum([a[i] * w[i] for i in range(7)]) % M
print(x)