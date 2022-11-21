import day10

def nice_print(table):
    for row in table:
        print("".join(row))

input_word = "oundnydw"
ones = 0

grid = [["." for _ in range(130)]]

for i in range(128):
    word = input_word + "-" + str(i)
    hash = day10.hashing(word)

    bitwise = ""
    for a in hash:
        binary = bin(int(a, 16))[2:]
        bitwise += "0" * (4-len(binary)) + binary
    ones += bitwise.count("1")
    
    # for b)
    bitwise = bitwise.replace("0", ".")
    bitwise = bitwise.replace("1", "#")
    grid.append(["."] + [x for x in bitwise] + ["."])


grid.append(["." for _ in range(130)])
neigh = [(-1, 0), (0, 1), (1, 0), (0, -1)]

region = 1
for j in range(130):
    for i in range(130):
        if grid[j][i] == "#":


            stack = [(j, i)]

            while stack:
                y, x = stack.pop()

                if grid[y][x] == str(region):
                    continue

                grid[y][x] = str(region)

                for n in neigh:
                    y_n = y + n[0]
                    x_n = x + n[1]
                    if grid[y_n][x_n] == "#":
                        stack.append((y_n, x_n))
            
            region += 1


nice_print(grid)
print("a: ", ones)
print("b: ", region-1)