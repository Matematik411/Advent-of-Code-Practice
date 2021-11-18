forb = []
while True:
    try:
        line = list(map(int, input().split("-")))
    except:
        break
    forb.append(line)
forb.sort()

#a)
higher = 0
for (l, u) in forb:
    if l > (higher+1):
        print("solution a: ", higher+1)
        break
    
    higher = max(higher, u)

#b)
allowed = 0
higher = 0
for (l, u) in forb:
    if l > (higher+1):
        allowed += (l - higher - 1)
    
    higher = max(higher, u)
print("solution b: ", allowed)