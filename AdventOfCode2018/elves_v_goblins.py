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
    
    def receive(self, x):
        self.hp -= x
        return self.hp <= 0

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

    def __init__(self, board, attack=3):
        self.board = board
        self.w = len(board[0])
        self.h = len(board)
        self.end = 0

        self.units = self.collect_units(attack)

        #a)
        #self.battle_simulation()
        #b)
        


    def battle_simulation(self):
        between = -1
        
        for round in range(5000):
            self.order = self.order_of_units()

            self.p = 0
            while self.p < len(self.order):
                (x, y) = self.order[self.p]
                if self.end:
                    between += 1
                else:
                    x_n, y_n = self.move(x, y)
                    self.attack(x_n, y_n)
                self.p += 1

            if self.end:
                print(self)
                ending = round
                if between < 0:
                    ending += 1
                if self.end == 1:
                    print("The winners are the ELVES!", ending)
                else:
                    print("The GOBLINS won.", ending)
                
                combat_sum = 0
                for u in self.units.values():
                    combat_sum += u.hp
                print("combat sum is ", combat_sum)
                print("result is ", ending * combat_sum)
                break
            print(self)

    def battle_no_elf_deaths(self, attack):    
        between = -1
        
        for round in range(5000):
            self.order = self.order_of_units()

            self.p = 0
            while self.p < len(self.order):
                (x, y) = self.order[self.p]
                if self.end:
                    between += 1
                else:
                    x_n, y_n = self.move(x, y)
                    self.attack_until_elf_death(x_n, y_n)
                self.p += 1

            if self.end:
                ending = round
                if between < 0:
                    ending += 1
                if self.end == 1:
                    print(self)
                    print("The winners are the ELVES - with no casualties!!!, round: ", ending, " ther attack was: ", attack)
                elif self.end == 2:
                    print("The GOBLINS won.", ending)
                else:
                    print("The ELF has died. :( attack: ", attack)
                
                combat_sum = 0
                for u in self.units.values():
                    combat_sum += u.hp
                print("combat sum is ", combat_sum)
                print("result is ", ending * combat_sum)
                return self.end
                
            
    
    def collect_units(self, attack):
        units = {}
        goblins = 0
        elves = 0
        for i in range(self.h):
            for j in range(self.w):
                x = self.board[i][j]
                if x == "E":
                    new = Unit(0, j, i, attack)
                    units[(j, i)] = new
                    elves += 1
                elif x == "G":
                    new = Unit(1, j, i)
                    units[(j, i)] = new
                    goblins += 1
        self.goblins = goblins
        self.elves = elves
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
        
    def adjacent(self, x, y, type):
        nghs = [self.board[y+self.dirs[i][1]][x+self.dirs[i][0]] for i in range(4)]
        if type == 0:
            return nghs.count("G") > 0
        else:
            return nghs.count("E") > 0

    def order_of_units(self):
        ord = []
        for i in range(self.h):
            for j in range(self.w):
                if self.board[i][j] in "EG":
                    ord.append((j, i))
        return ord

    def move(self, x, y):
        u = self.units[(x, y)]

        if self.adjacent(x, y, u.type):
            return x, y

        #bfs for a move
        q = Queue()
        visited = set()
        q.put([x, y, ""])
        target = []
        while not q.empty():
            a, b, s = q.get()
            if target and len(s) > len(target[2]):
                break
            if self.adjacent(a, b, u.type):
                if target:
                    if (b, a) < (target[1], target[0]):
                        target = [a, b, s]
                else:
                    target = [a, b, s]
            
            for i in range(4):
                x_n = a + self.dirs[i][0]
                y_n = b + self.dirs[i][1]
                if self.board[y_n][x_n] == "." and (x_n, y_n) not in visited:
                    visited.add((x_n, y_n))
                    q.put([x_n, y_n, s + str(i)])
            
        if not target:
            return x, y

        m = int(target[2][0])
        x_n = x + self.dirs[m][0]
        y_n = y + self.dirs[m][1]
        u.move_to(x_n, y_n)
        self.units.pop((x, y))
        self.units[(x_n, y_n)] = u
        self.board[y][x] = "."
        self.board[y_n][x_n] = "E" if u.type == 0 else "G"
        return x_n, y_n

    def attack(self, x, y):
        u = self.units[(x, y)]
        target_hp = 201
        target = None
        for i in range(4):
            x_n = x + self.dirs[i][0]
            y_n = y + self.dirs[i][1]
            if self.board[y_n][x_n] == ("G" if u.type == 0 else "E"):
                neigh = self.units[(x_n, y_n)]
                if neigh.hp < target_hp:
                    target = [neigh, x_n, y_n]
                    target_hp = neigh.hp
        if target:
            target, x_n, y_n = target
            if target.receive(u.att): #if it dies
                self.units.pop((x_n, y_n))
                self.board[y_n][x_n] = "."
                if self.order.index((x_n, y_n)) < self.p:
                    self.p -= 1
                self.order.remove((x_n, y_n))
                if target.type == 1:
                    self.goblins -= 1
                    if self.goblins == 0:
                        self.end = 1
                else:
                    self.elves -= 1
                    if self.elves == 0:
                        self.end = 2
    
    def attack_until_elf_death(self, x, y):
        u = self.units[(x, y)]
        target_hp = 201
        target = None
        for i in range(4):
            x_n = x + self.dirs[i][0]
            y_n = y + self.dirs[i][1]
            if self.board[y_n][x_n] == ("G" if u.type == 0 else "E"):
                neigh = self.units[(x_n, y_n)]
                if neigh.hp < target_hp:
                    target = [neigh, x_n, y_n]
                    target_hp = neigh.hp
        if target:
            target, x_n, y_n = target
            if target.receive(u.att): #if it dies
                self.units.pop((x_n, y_n))
                self.board[y_n][x_n] = "."
                if self.order.index((x_n, y_n)) < self.p:
                    self.p -= 1
                self.order.remove((x_n, y_n))
                if target.type == 1:
                    self.goblins -= 1
                    if self.goblins == 0:
                        self.end = 1
                else:
                    self.elves -= 1
                    self.end = 3
                    if self.elves == 0:
                        self.end = 2

            

world = []
for _ in range(32):
    world.append([x for x in input()])
#a)
#world = World(world)

#b)
a = 4
while True:
    copy = []
    for l in world:
        copy.append([x for x in l])
    w = World(copy, a)
    res = w.battle_no_elf_deaths(a)
    if res > 1:
        a += 1
    else:
        break

