class Int_code:
    def __init__(self, s):
        memory = {}
        nrs = map(int, s.split(","))
        for i, x in enumerate(nrs):
            memory[i] = x
        self.memory = memory
    
    def set(self, i, x):
        self.memory[i] = x
    
    def one(self, a, b, c):
        self.memory[c] = self.memory[a] + self.memory[b]
    def two(self, a, b, c):
        self.memory[c] = self.memory[a] * self.memory[b]

    def run(self, start):
        i = start
        while True:
            c = self.memory[i]

            if c == 99:
                break
            if c == 1:
                self.one(self.memory[i+1], self.memory[i+2], self.memory[i+3])
                i += 4
            elif c == 2:
                self.two(self.memory[i+1], self.memory[i+2], self.memory[i+3])
                i += 4
        
        return self.memory[0]

start = input()
#part one
computer = Int_code(start)
computer.set(1, 12)
computer.set(2, 2)
print(computer.run(0))

#part two
target = 19690720
for noun in range(1, 100):
    for verb in range(1, 100):
        computer = Int_code(start)
        computer.set(1, noun)
        computer.set(2, verb)
        if computer.run(0) == target:
            print(100*noun + verb)