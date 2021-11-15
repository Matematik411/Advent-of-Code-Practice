number_possible = 0

while True:
    try:
        case1 = list(map(int, input().split()))
        case2 = list(map(int, input().split()))
        case3 = list(map(int, input().split()))
    except:
        break

    tri1 = [case1[0], case2[0], case3[0]]
    tri2 = [case1[1], case2[1], case3[1]]
    tri3 = [case1[2], case2[2], case3[2]]

    tri1.sort()
    tri2.sort()
    tri3.sort()

    if tri1[0] + tri1[1] > tri1[2]:
        number_possible += 1
    if tri2[0] + tri2[1] > tri2[2]:
        number_possible += 1
    if tri3[0] + tri3[1] > tri3[2]:
        number_possible += 1

#a = 917
print(number_possible)