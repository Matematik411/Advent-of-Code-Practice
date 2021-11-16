def check_abba(s):
    for i in range(len(s)-3):
        a, b, c, d = s[i:i+4]

        if (a == d) and (b == c) and (a != b):
            return True
    return False

def gather_aba(s):
    aba = set()
    for i in range(len(s)-2):
        a, b, c = s[i:i+3]
        
        if (a == c) and (a != b):
            aba.add(a+b+c)

    return aba

def check_aba(fst, snd):
    for (a, b, _) in fst:
        if (b+a+b) in snd:
            return True
    
    return False

supporters_tls = 0
supporters_ssl = 0

while True:
    try:
        line = input()
    except:
        break

    part = ""
    #a)
    outside = False
    inside = False
    #b)
    out_aba = set()
    in_aba = set()

    for x in line:
        if x == "[":
            if check_abba(part):
                outside = True

            out_aba.update(gather_aba(part))

            part = ""
            
        elif x == "]":
            if check_abba(part):
                inside = True

            in_aba.update(gather_aba(part))

            part = ""

        else:
            part += x

    if check_abba(part):
        outside = True
    out_aba.update(gather_aba(part))

    if outside and (not inside):
        supporters_tls += 1
    
    if check_aba(out_aba, in_aba):
        supporters_ssl += 1

print(supporters_tls)
print(supporters_ssl)

