import re

real_room_sum = 0

while True:
    try:
        line = input()
    except:
        break

    name, id, checksum = re.match(r"(.*)-(\d*)\[(.....)\]", line).groups()
    
    #a)

    name_changed = name.replace("-", "")
    name_chars = {}
    for x in name_changed:
        if x in name_chars:
            name_chars[x] += 1
        else:
            name_chars[x] = 1
    name_chars = list(name_chars.items())
    name_chars.sort()
    name_chars.sort(key = lambda x: -x[1])
    if "".join([x[0] for x in name_chars[:5]]) == checksum:
        real_room_sum += int(id)
    else:
        continue

    #b)
    code = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k', 'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p', 'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u', 'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 'z': 'a', '-': ' ', ' ': ' '}

    def rotate(letter, times):
        for _ in range(times):
            letter = code[letter]
        return letter

    real_name = ""
    for x in name:
        real_name += rotate(x, int(id))

    print(real_name, id, checksum)

print(real_room_sum)
#b) northpole object storage 501 hmxka

