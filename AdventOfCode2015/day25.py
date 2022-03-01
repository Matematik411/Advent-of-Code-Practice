def next_value(x):
    x *= 252533
    x %= 33554393
    return x

#target= [column,row]
target = [3075, 2981]

k = 1
found = False
value = 20151125  
while not found:

    for i in range(1, k+1):
        coords = [i, k+1-i]
        
        if coords == target:
            print(value)
            found = True
            break

        value = next_value(value)

    k += 1
