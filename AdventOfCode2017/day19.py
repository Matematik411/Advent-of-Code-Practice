import sys
file = sys.stdin.read()

map = file.split("\n")

position = [0, map[0].index("|")]
direction = [1, 0]
collected_word = ""

steps = 0

while True:
    piece = map[position[0]][position[1]]

    if piece == "+":
        if direction[0] != 0:
            # if we are travelling vertically
            if map[position[0]][position[1] - 1] != " ":
                direction = [0, -1]
            else:
                direction = [0, 1]
        else:
            if map[position[0] - 1][position[1]] != " ":
                direction = [-1, 0]
            else:
                direction = [1, 0]
        
    elif piece not in ["|", "-"]:
        # letter
        collected_word += piece

        around = 0
        for (dy, dx) in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
            if map[position[0]+dy][position[1]+dx] != " ":
                around += 1
        if around == 1:
            steps += 1
            break


    position[0] += direction[0]
    position[1] += direction[1]
    steps += 1

print("a: ", collected_word)
print("b: ", steps)
