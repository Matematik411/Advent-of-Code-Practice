stream = input()
d = len(stream)

# a)
score = 0
group_value = 0
# b)
trash_characters = 0


i = 0
garbage = False
while i < d:
    c = stream[i]

    if garbage:
        if c == ">":
            garbage = False
        elif c == "!":
            i += 1
        else:
            trash_characters += 1
    
    else:
        if c == "{":
            group_value += 1
        elif c == "}":
            score += group_value
            group_value -= 1
        elif c == "<":
            garbage = True
    
    i += 1

print("a: ", score)
print("b: ", trash_characters)


