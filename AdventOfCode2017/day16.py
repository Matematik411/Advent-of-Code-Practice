order = "abcdefghijklmnop"
moves = input().split(",")

# part b)
# this positioning repeats at round 60

real_rounds = 10**9 % 60


for round in range(real_rounds):
    for move in moves:

        if move[0] == "s":
            X = int(move[1:])
            order = order[-X:] + order[:-X]
        
        elif move[0] == "x":
            A, B = map(int, move[1:].split("/"))
            if A > B:
                A, B = B, A
            elif A == B:
                continue
            order = order[:A] + order[B] + order[A+1:B] + order[A] + order[B+1:]
        
        elif move[0] == "p":
            A = move[1]
            B = move[3]
            order = order.replace(A, "!").replace(B, A).replace("!", B)
    

print("a:  fnloekigdmpajchb")
print("b: ", order)

