from itertools import permutations

class Int_code:
    def __init__(self, s, inputs):
        memory = {}
        nrs = map(int, s.split(","))
        for i, x in enumerate(nrs):
            memory[i] = x
        self.memory = memory
        self.inputs = inputs
        self.outputs = []
    
    def set(self, i, x):
        self.memory[i] = x
    
    def one(self, a, b, c, modes):
        if modes % 10 == 0:
            a = self.memory[a]
        modes //= 10
        if modes % 10 == 0:
            b = self.memory[b]
        self.memory[c] = a + b
    def two(self, a, b, c, modes):
        if modes % 10 == 0:
            a = self.memory[a]
        modes //= 10
        if modes % 10 == 0:
            b = self.memory[b]
        self.memory[c] = a * b
    def three(self, a, modes):
        x = self.inputs.pop(0)
        self.memory[a] = x
    def four(self, a, modes):
        if modes % 10 == 0:
            a = self.memory[a]
        self.outputs.append(a)
    def five(self, a, b, modes):
        if modes % 10 == 0:
            a = self.memory[a]
        modes //= 10
        if modes % 10 == 0:
            b = self.memory[b]
        if a != 0:
            return (True, b)
        else:
            return (False, 0)
    def six(self, a, b, modes):
        if modes % 10 == 0:
            a = self.memory[a]
        modes //= 10
        if modes % 10 == 0:
            b = self.memory[b]
        if a == 0:
            return (True, b)
        else:
            return (False, 0)
    def seven(self, a, b, c, modes):
        if modes % 10 == 0:
            a = self.memory[a]
        modes //= 10
        if modes % 10 == 0:
            b = self.memory[b]
        self.memory[c] = 1 if (a < b) else 0
    def eight(self, a, b, c, modes):
        if modes % 10 == 0:
            a = self.memory[a]
        modes //= 10
        if modes % 10 == 0:
            b = self.memory[b]
        self.memory[c] = 1 if (a == b) else 0
    def add_inputs(self, inp):
        for x in inp:
            self.inputs.append(x)

    def run(self, start):
        i = start
        while True:
            print(i)
            c = self.memory[i]
            modes = c // 100
            c %= 100
            # print(i, self.memory[i])

            if c == 99:
                break
            elif c == 1:
                self.one(self.memory[i+1], self.memory[i+2], self.memory[i+3], modes)
                i += 4
            elif c == 2:
                self.two(self.memory[i+1], self.memory[i+2], self.memory[i+3], modes)
                i += 4
            elif c == 3:
                print(i)
                self.three(self.memory[i+1], modes)
                i += 2
            elif c == 4:
                self.four(self.memory[i+1], modes)
                i += 2
            elif c == 5:
                sol = self.five(self.memory[i+1], self.memory[i+2], modes)
                if sol[0]:
                    i = sol[1]
                else:
                    i += 3
            elif c == 6:
                sol = self.six(self.memory[i+1], self.memory[i+2], modes)
                if sol[0]:
                    i = sol[1]
                else:
                    i += 3
            elif c == 7:
                self.seven(self.memory[i+1], self.memory[i+2], self.memory[i+3], modes)
                i += 4
            elif c == 8:
                self.eight(self.memory[i+1], self.memory[i+2], self.memory[i+3], modes)
                i += 4
        
        return self.outputs

start = input()

# # part one
# max_power = 0
# settings = [0, 1, 2, 3, 4]
# for p in permutations(settings):
#     c_inp = [p[0], 0, p[1], 0, p[2], 0, p[3], 0, p[4], 0]
#     for i in range(5):
#         computer = Int_code(start, c_inp)
#         if i < 4:
#             c_inp[1] = computer.run(0)[0]
#         else:
#             c_inp = computer.run(0)[0]
#     if c_inp > max_power:
#         max_power = c_inp
#         print(max_power)

# part two
max_power_2 = 0
settings = [5, 6, 7, 8, 9]
for p in permutations(settings):
    print(p)
    pc_a = Int_code(start, [p[0], 0])
    nxt = pc_a.run(0)[0]

    pc_b = Int_code(start, [p[1], nxt])
    nxt = pc_b.run(0)[0]

    pc_c = Int_code(start, [p[2], nxt])
    nxt = pc_c.run(0)[0]

    pc_d = Int_code(start, [p[3], nxt])
    nxt = pc_d.run(0)[0]

    pc_e = Int_code(start, [p[4], nxt])
    nxt = pc_e.run(0)

    stop = False
    last = 0
    while not stop:
        try:
            pc_a.add_inputs(nxt)
            nxt = pc_a.run(0)
            pc_b.add_inputs(nxt)
            nxt = pc_b.run(0)
            pc_c.add_inputs(nxt)
            nxt = pc_c.run(0)
            pc_d.add_inputs(nxt)
            nxt = pc_d.run(0)
            pc_e.add_inputs(nxt)
            nxt = pc_e.run(0)
            last = nxt[0]
        except:
            stop = True
    
    if last > max_power_2:
        max_power_2 = last
        print(max_power_2)


