import itertools
import numpy as np
import operator

packages = []
while True:
    try:
        a = int(input())
    except:
        break
    packages.append(a)

n = len(packages) 
# target = sum(packages) // 3
target = sum(packages) // 4

def prod(l):
    p = 1
    for x in l:
        p *= x
    return p

def correct_sum(p, k): 

    for size in range(1, len(p)):
        Q = prod(p)
        for fst in itertools.combinations(p, size):
            if sum(fst) == target:

                if k == 2:
                    return True
                
                if k > 2:
                    print(fst)

                    # if correct_sum(list(set(p) - set(fst)), k - 1):
                    curr_Q = prod(fst)
                    print(curr_Q)
                    if curr_Q < Q:
                        Q = curr_Q

        if Q != prod(p):
            return Q




print(correct_sum(packages, 4))