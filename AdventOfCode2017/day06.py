banks = list(map(int, input().split()))

# previous = set()

# changed for b
target = [1, 1, 0, 15, 14, 13, 12, 10, 10, 9, 8, 7, 6, 4, 3, 5]
banks = [1, 1, 0, 15, 14, 13, 12, 10, 10, 9, 8, 7, 6, 4, 3, 5]
size = 0

while True:

    # previous.add(tuple(banks))

    max_i = banks.index(max(banks))
    amount = banks[max_i]
    banks[max_i] = 0

    for j in range(1, 17):
        banks[(max_i + j) % 16] += (amount // 16) + (1 if j <= (amount % 16) else 0)

    size += 1

    if banks == target:
        print("b: ", size)
        break
        

print("a: ", 14029)
# print("a: ", len(previous))
# the repeated is [1, 1, 0, 15, 14, 13, 12, 10, 10, 9, 8, 7, 6, 4, 3, 5]