scanners = {}
while True:
    try:
        line = input()
    except EOFError:
        break
    a, b = line.split()
    scanners[int(a[:-1])] = int(b)


# a)

def adventure(delay):
    severity = 0

    pos = 0
    while pos < 93:
        if scanners.get(pos, 0):
            scanner_in_pos = ((pos + delay) % (2 * (scanners[pos] - 1))) == 0
            
            if scanner_in_pos:
                severity += pos * scanners[pos]
                if pos == 0:
                    # so the part b) detects the "getting caught by scanner 0"
                    severity += 0.5
        
        pos += 1
    
    return severity

print("a: ", adventure(0))

# b)
for dt in range(10000000):
    result = adventure(dt)
    # print(result)
    if result == 0:
        print("b: ", dt)
        break
