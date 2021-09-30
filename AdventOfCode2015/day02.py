skupno = 0

trak = 0

darilo = input()

while True:
    darilo = sorted(list(map(int, darilo.split("x"))))

    a, b, c = darilo

    skupno += 2*(a*b + a*c + b*c)
    skupno += a*b

    trak += 2*(a + b)
    trak += a*b*c

    try:
        darilo = input()
    except EOFError:
        break


print("papir: " + str(skupno))
print("trak: " + str(trak))