import sys
file = sys.stdin.read().split("\n")

twos_raw = [[x for x in r.split(" => ")] for r in file[:6]]
threes_raw = [[x for x in r.split(" => ")] for r in file[6:]]

twos = [[[[x for x in r] for r in image.split("/")] for image in pair] for pair in twos_raw]

threes = [[[[x for x in r] for r in image.split("/")] for image in pair] for pair in threes_raw]


def rotate(t):
    N = len(t)
    
    if N == 2:
        return [
            [t[0][1], t[1][1]], 
            [t[0][0], t[1][0]]
        ]
    else:
        return [
            [t[0][2], t[1][2], t[2][2]],
            [t[0][1], t[1][1], t[2][1]],
            [t[0][0], t[1][0], t[2][0]]
        ]

def mirror(table):
    new = []
    for i in range(len(table)):
        new.append(table[-i-1])
    return new


def compare(cut, example):

    for m in range(2):
        for r in range(4):
            cut = rotate(cut)

            if cut == example:
                return True
            
            if r == 3:
                cut = mirror(cut)
    
    return False




def enhance(image, s):
    if s == 2:
        database = twos
    else:
        database = threes

    for sample in database:
        if compare(image, sample[0]):
            return sample[1]
    
    print("ERROR --- NO MATCH !!!")
    




picture = [[".", "#", "."], [".", ".", "#"], ["#", "#", "#"]]

for round in range(18):
    size = len(picture)
    if size % 2 == 0:
        grid = size // 2
        sq_side = 2
    else:
        grid = size // 3
        sq_side = 3
    
    # couting order in the grid
    # 1 | 2 | 3
    # 4 | 5 | 6
    # 7 | 8 | 9
    parts = []
    for j in range(grid):
        for i in range(grid):
            section = [
                [
                    picture[j*sq_side + y][i*sq_side + x] 
                    for x in range(sq_side)
                ]
                for y in range(sq_side)
            ]
            parts.append(section)

    increased = []

    for section in parts:
        
        increased.append(enhance(section, sq_side))


    new_picture = []

    for j in range((sq_side+1) * grid):
        sk = j // (sq_side+1)
        line = []
        for k in range(grid):
            line += increased[sk*grid + k][j % (sq_side+1)]
        new_picture.append(line)
    

    print("round: ", round, "size: ", len(new_picture))
    picture = new_picture
        
    pixels_on = sum([row.count("#") for row in picture])                  
    if round == 4:
        print("a: ", pixels_on)
    if round == 17:
        print("b: ", pixels_on)


