trap = {"^^.", ".^^", "^..", "..^"}

floor = input()
safe = floor.count(".")
w = len(floor)
for _ in range(399999):
    new = ""
    curr = ".." + floor[0]
    for j in range(w-1):
        curr = curr[1:] + floor[j+1]
        if curr in trap:
            new += "^"
        else:
            new += "."
            safe += 1
    curr = curr[1:] + "."
    if curr in trap:
        new += "^"
    else:
        new += "."
        safe += 1
    
    floor = new
    print(floor)
#a = 2016
print("solution b: ", safe)
