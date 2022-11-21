# a: 40132
# 
# changed for b) 

def hashing(code):
    N = 256
    data = [i for i in range(N)]
    position = 0
    lengths = [ord(x) for x in code] + [17, 31, 73, 47, 23]
    skip_size = 0

    def reverse(j, l):
        for k in range(l // 2):
            data[(j+k)%N], data[(j+l-1-k)%N] = data[(j+l-1-k)%N], data[(j+k)%N]


    for round in range(64):
        for length in lengths:
            reverse(position, length)
            position = (position + length + skip_size) % N
            skip_size = (skip_size + 1) % N

    dense_hash = [0 for _ in range(16)]

    for i in range(16):
        for j in range(16):
            dense_hash[i] = dense_hash[i] ^ data[16*i + j]

    knot_hash = ""

    for nr in dense_hash:
        hexa = hex(nr)[2:]
        if len(hexa) == 1:
            hexa = "0" + hexa
        
        knot_hash += hexa
    
    return knot_hash
    

# print("a: ", 40132)
# print("b: ", hashing(input()))
