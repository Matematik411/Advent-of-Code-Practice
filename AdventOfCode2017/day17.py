steps = 363

spinlock = {0: 1, 1: 0}
position = 1

for n in range(2, 2018):
    
    # make steps
    current_steps = steps % n
    for _ in range(current_steps):
        position = spinlock[position]

    # insert n
    next_node = spinlock[position]
    spinlock[position] = n
    spinlock[n] = next_node
    position = n


print("a: ", spinlock[2017])
    

# part b)
# now look at it as a list with list[0] = 0

after_zero = 1
position = 1

for n in range(2, 50000001):

    position = (position + steps) % n

    if position == 0:
        after_zero = n
    
    position += 1

print("b: ", after_zero)