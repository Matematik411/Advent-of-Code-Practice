from collections import defaultdict
import sys
file = sys.stdin.read()

rules = [r.split() for r in file.split("\n")]
R = len(rules)
print("a:  3423")
# changed for b)

registers = [defaultdict(lambda: 0) for _ in range(2)]

registers[0]["p"] = 0
registers[1]["p"] = 1

send_queue = [[] for _ in range(2)]
send_size = [0, 0]
positions = [0, 0]

def value_of(m, a):
    try:
        return int(a)
    except:
        return registers[m][a]

c_m = 0


while 0 <= positions[c_m] < R:
    r, *d = rules[positions[c_m]]

    if r == "snd":
        x = d[0]
        send_queue[c_m].append(value_of(c_m, x))
        send_size[c_m] += 1
    elif r == "set":
        x, y = d
        registers[c_m][x] = value_of(c_m, y)
    elif r == "add":
        x, y = d
        registers[c_m][x] += value_of(c_m, y)
    elif r == "mul":
        x, y = d
        registers[c_m][x] *= value_of(c_m, y)
    elif r == "mod":
        x, y = d
        registers[c_m][x] %= value_of(c_m, y)
    elif r == "rcv":
        x = d[0]
        # is there anything to be received?
        if send_queue[1-c_m]:
            value = send_queue[1-c_m].pop(0)
            registers[c_m][x] = value
        else:
            c_m = 1 - c_m
            # so the position is correct
            positions[c_m] -= 1
            if send_queue == [[], []]:
                print("b: ", send_size[1])
                break   
    elif r == "jgz":
        x, y = d
        if value_of(c_m, x) > 0:
            positions[c_m] += value_of(c_m, y) - 1

    positions[c_m] += 1



        


