from queue import Queue

navodila = {}
vrsta = Queue()
vrednosti = {}

while True:
    try:
        line = input().split()
    except:
        break

    if len(line) == 5:
        cilj = line[-1]

        a, b = line[0], line[2]
        op = line[1]

        neznani = 2
        if a.isdigit():
            neznani -= 1
            a = int(a)
            
        if b.isdigit():
            neznani -= 1
            b = int(b)
        
        navodila[cilj] = [a, b, op, neznani]
  
    elif len(line) == 4:
        cilj = line[-1]

        a = line[1]
        op = line[0]

        neznani = 1
        if a.isdigit():
            neznani -= 1
            a = int(a)
        
        navodila[cilj] = [a, op, neznani]
        
    else:
        cilj = line[-1]

        a = line[0]

        neznani = 1
        if a.isdigit():
            neznani -= 1
            a = int(a)

        if neznani == 0:
            vrsta.put(
                [cilj, a]
            )
        
        navodila[cilj] = [a, neznani]

def naloga_and(c, a, b):
    if isinstance(a, str):
        a = vrednosti[a]
    if isinstance(b, str):
        b = vrednosti[b]
    
    vrednosti[c] = a & b
    
def naloga_or(c, a, b):
    if isinstance(a, str):
        a = vrednosti[a]
    if isinstance(b, str):
        b = vrednosti[b]
    
    vrednosti[c] = a | b

def naloga_rshift(c, a, b):
    if isinstance(a, str):
        a = vrednosti[a]
    if isinstance(b, str):
        b = vrednosti[b]
    
    vrednosti[c] = a >> b

def naloga_lshift(c, a, b):
    if isinstance(a, str):
        a = vrednosti[a]
    if isinstance(b, str):
        b = vrednosti[b]
    
    vrednosti[c] = a << b

def naloga_not(c, a):
    if isinstance(a, str):
        a = vrednosti[a]
    vrednosti[c] = ~a + 2**16

def naloga_save(c, a):
    if isinstance(a, str):
        a = vrednosti[a]
    
    vrednosti[c] = a


while not vrsta.empty():
    delo = vrsta.get()
    print(delo[0])

    if "AND" in delo:
        naloga_and(
            delo[0],
            delo[1],
            delo[2]
        )
    elif "OR" in delo:
        naloga_or(
            delo[0],
            delo[1],
            delo[2]
        )
    elif "RSHIFT" in delo:
        naloga_rshift(
            delo[0],
            delo[1],
            delo[2]
        )            
    elif "LSHIFT" in delo:
        naloga_lshift(
            delo[0],
            delo[1],
            delo[2]
        )
    elif "NOT" in delo:
        naloga_not(
            delo[0],
            delo[1]
        )
    else:
        naloga_save(
            delo[0],
            delo[1]
        )

    navodila.pop(delo[0])

    for (k, v) in navodila.items():
        if delo[0] in v:
            v[-1] -= 1
            if v[-1] == 0:
                vrsta.put(
                    [k] + v[:-1]
                )

print(vrednosti["a"])
#a) a = 16076