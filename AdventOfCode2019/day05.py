class Int_code:
    def __init__(self, s, inputs):
        memory = {}
        nrs = map(int, s.split(","))
        for i, x in enumerate(nrs):
            memory[i] = x
        self.memory = memory
        self.inputs = inputs
    
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
        print(a)
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

    def run(self, start):
        i = start
        while True:
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
        
        return self.memory[0]

start = input()
# part one
inputs_1 = [1]
computer = Int_code(start, inputs_1)
computer.run(0)


# part two
inputs_2 = [5]
computer = Int_code(start, inputs_2)
computer.run(0)

# # test
# inputs = [3]
# computer = Int_code(start, inputs)
# computer.run(0)
