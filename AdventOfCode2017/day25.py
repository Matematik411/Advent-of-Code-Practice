from collections import defaultdict
# A B C D E F
# 0 1 2 3 4 5
rules = {
    # N x S -> N x S x +-1
    (0, 0): (1, 1, 1),
    (1, 0): (0, 2, -1),
    (0, 1): (1, 0, -1),
    (1, 1): (1, 3, -1),
    (0, 2): (1, 3, 1),
    (1, 2): (0, 2, 1),
    (0, 3): (0, 1, -1),
    (1, 3): (0, 4, 1),
    (0, 4): (1, 2, 1),
    (1, 4): (1, 5, -1),
    (0, 5): (1, 4, -1),
    (1, 5): (1, 0, 1),
}

steps = 12656374
tape = defaultdict(lambda: 0)
head = 0
state = 0

for count in range(steps):
    x_n, s_n, d = rules[(tape[head], state)]

    state = s_n
    tape[head] = x_n
    head += d

    if count % 1000000 == 0:
        print(count)
print("a: ", sum(tape.values()))

