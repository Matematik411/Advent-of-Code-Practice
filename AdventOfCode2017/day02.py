spreadsheet = []

while True:
    try:
        line = input()
    except EOFError:
        break
    spreadsheet.append(list(map(int, line.split())))

# a)
checksum = sum([max(line) - min(line) for line in spreadsheet])

print("a: ", checksum)

# b)
checksum_b = 0
for line in spreadsheet:
    for i in range(len(line)):
        found = False
        for j in range(i+1, len(line)):
            a = max(line[i], line[j])
            b = min(line[i], line[j])

            if a % b == 0:
                checksum_b += a // b
                found = True
                break
        if found:
            break

print("b: ", checksum_b)