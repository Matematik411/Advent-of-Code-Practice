location = 0
inputs = []

while True:
    try:
        case = int(input())
        inputs.append(case)
        location += case
    except EOFError:
        break

print("a: " + str(location))

location = 0
already = set()

end = False

while (not end):
    for x in inputs:
        location += x
        if (location in already) and (not end):
            print("b: " + str(location))
            end = True
        already.add(location)