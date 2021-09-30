oklepaji = input()

nadstropje = 0
polozaj = 0
klet = -1


for znak in oklepaji:
    polozaj += 1
    if znak == "(":
        nadstropje += 1
    else:
        nadstropje -= 1

    if (nadstropje == -1) and (klet == -1):
        klet = polozaj

print(nadstropje)
print(klet)