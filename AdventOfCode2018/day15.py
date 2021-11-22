from queue import Queue


class Unit:
    # Elvse type = 0
    # Goblins type = 1
    def __init__(self, type, x, y, attack=3, health=200):
        self.type = type
        self.att = attack
        self.hp = health
        self.x = x
        self.y = y

    def move_to(self, a, b):
        self.x = a
        self.y = b

    def __str__(self) -> str:
        pict = ""
        if self.type == 0:
            pict += "E("
        else:
            pict += "G("
        pict += str(self.hp) + ")"
        return pict

# -------------------------------------------------
class World:
    dirs = [[0, -1], [-1, 0], [1, 0], [0, 1]]

    def __init__(self, board):
        self.board = board
        self.w = len(board[0])
        self.h = len(board)
        self.units = self.collect_units()
        self.order = self.order_of_units()
        self.adjacents = self.adjacents_of_units() #this one is updated after each move
        print(self)
        self.part_one()

    def part_one(self):
        
        self.moving()
        print(self)
        print(".....................................................")
        
        self.order = self.order_of_units()
        self.moving()
        print(self)


    
    def collect_units(self):
        units = {}
        for i in range(self.h):
            for j in range(self.w):
                x = self.board[i][j]
                if x == "E":
                    new = Unit(0, j, i)
                    units[(j, i)] = new
                elif x == "G":
                    new = Unit(1, j, i)
                    units[(j, i)] = new
        return units

    def __str__(self):
        pict = ""
        for i in range(self.h):
            pict += "".join(self.board[i])
            for j in range(self.w):
                if self.board[i][j] in "EG":
                    pict += "  " + str(self.units[(j, i)])
            pict += "\n"
        return pict
        
    def adjacents_of_units(self):
        # adj = [[adjacents of elves], [adjacents of goblins]]
        adj = [set(), set()]

        for (x, y) in self.units:
            t = self.units[(x, y)].type
            for i in range(4):
                x_n = x + self.dirs[i][0]
                y_n = y + self.dirs[i][1]
                if self.board[y_n][x_n] == ".":
                    adj[t].add((x_n, y_n))
        return adj

    def order_of_units(self):
        ord = []
        for i in range(self.h):
            for j in range(self.w):
                if self.board[i][j] in "EG":
                    ord.append((j, i))
        return ord

    def moving(self):
        for (x, y) in self.order:
            print(self)
            u = self.units[(x, y)]

            no_move = False
            for i in range(4):
                x_n = x + self.dirs[i][0]
                y_n = y + self.dirs[i][1]
                if self.board[y_n][x_n] == ("G" if u.type == 0 else "E"):
                    no_move = True
            if no_move:
                continue

            q = Queue()
            visited = set()
            q.put([x, y, ""])
            target = []
            while not q.empty():
                a, b, s = q.get()
                if (a, b) in self.adjacents[1-u.type]:
                    target = [a, b, s]
                    break
                
                for i in range(4):
                    x_n = a + self.dirs[i][0]
                    y_n = b + self.dirs[i][1]
                    if self.board[y_n][x_n] == "." and (x_n, y_n) not in visited:
                        visited.add((x_n, y_n))
                        q.put([x_n, y_n, s + str(i)])
                
            if not target:
                continue

            m = int(target[2][0])
            x_n = x + self.dirs[m][0]
            y_n = y + self.dirs[m][1]
            u.move_to(x_n, y_n)
            self.units.pop((x, y))
            self.units[(x_n, y_n)] = u
            self.board[y][x] = "."
            self.board[y_n][x_n] = "E" if u.type == 0 else "G"

            #first remove old adj
            for i in range(4):
                x_nn = x + self.dirs[i][0]
                y_nn = y + self.dirs[i][1]
                if self.board[y_nn][x_nn] in "EG.":
                    rem = True
                    for j in range(4):
                        a = x_nn + self.dirs[j][0]
                        b = y_nn + self.dirs[j][1]
                        if self.board[b][a] == ("E" if u.type == 0 else "G"):
                            rem = False
                    if rem:
                        self.adjacents[u.type].discard((x_nn, y_nn))
            #add new
            for i in range(4):
                x_nn = x_n + self.dirs[i][0]
                y_nn = y_n + self.dirs[i][1]
                if self.board[y_nn][x_nn] == ".":
                    self.adjacents[u.type].add((x_nn, y_nn))

            



# world = [["#","#","#","#","#","#","#"],
# ["#",".","E",".",".",".","#"],
# ["#",".",".",".",".",".","#"],
# ["#",".",".",".","G",".","#"],
# ["#","#","#","#","#","#","#"]]
world = []
for _ in range(9):
    world.append([x for x in input()])
world = World(world)
