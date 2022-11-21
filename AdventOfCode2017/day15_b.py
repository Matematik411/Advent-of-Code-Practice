a = 873
b = 583

lense = 2 ** 16

module = 2147483647 
factor_a = 16807 
factor_b = 48271

judge = 0

for round in range(5*(10**6)):
    a = (a * factor_a) % module
    while a % 4 != 0:
        a = (a * factor_a) % module
    b = (b * factor_b) % module
    while b % 8 != 0:
        b = (b * factor_b) % module


    if a % lense == b % lense:
        judge += 1

    if round % 100000 == 0:
        print(round, judge)

print("b: ", judge)

