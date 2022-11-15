valids = 0
valids_b = 0

while True:
    try:
        password = input()
    except EOFError:
        break

    # a)
    if len(password.split()) == len(set(password.split())):
        valids += 1

    # b)
    words = []
    for word in password.split():
        if set(word) in words:
            break
        else:
            words.append(set(word))
    if len(password.split()) == len(words):
        valids_b += 1


print("a: ", valids)
print("b: ", valids_b)