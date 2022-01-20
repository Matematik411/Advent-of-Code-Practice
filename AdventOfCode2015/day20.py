input = 29000000
meja = input//10
hise = [0 for i in range(meja+1)]

#deljenje daril
for d in range(1, meja): # d ... številka škrata
    k = d
    while k < meja and k <= 50 * d:
        hise[k] += 11*d
        k += d

# poisce najmanjso
for i in range(meja+1):
    if hise[i] >= input:
        print(i)
        print(hise[i])
        break
