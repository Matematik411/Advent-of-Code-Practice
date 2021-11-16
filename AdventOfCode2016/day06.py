code = ""
code2 = ""

data = []

while True:
    try:
        data.append(input())
    except:
        break

for i in range(len(data[0])):
    freq = {}

    for word in data:
        if word[i] in freq:
            freq[word[i]] += 1
        else:
            freq[word[i]] = 1

    code += sorted([x for x in freq.items()],key= lambda x: -x[1])[0][0]
    code2 += sorted([x for x in freq.items()],key= lambda x: x[1])[0][0]

print(code)
print(code2)
    
