doubles = 0
triples = 0
words = []

def duplicates(s):
    rep = {}
    for l in s:
        if l in rep:
            rep[l] += 1
        else:
            rep[l] = 1
    return rep

while True:
    try:
        word = input()
    except:
        break
    
    d = duplicates(word)
    if 2 in d.values():
        doubles +=1
    if 3 in d.values():
        triples +=1
    
    words.append(word)

print("a: " + str(doubles * triples))

def check(l, r):
    mistake = False
    same_chars = ""

    for i in range(len(l)):
        if l[i] != r[i]:
            if mistake:
                return False
            else:
                mistake = True
        else:
            same_chars += l[i]

    return same_chars


end = False
for i in range(len(words)):
    fst = words[i]
    for snd in words[i+1:]:
        test = check(fst, snd)
        if test:
            print("b: " + test)
            end = True
            break
    
    if end:
        break
