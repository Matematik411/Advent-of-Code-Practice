from queue import Queue
fav = 1362

def is_open(x, y):
    if x*y < 0:
        return False
    n = x*x + 3*x + 2*x*y + y + y*y
    n += fav
    n = bin(n).count("1")
    return n % 2 == 0

dirs = [[1, 0], [0, -1], [-1, 0], [0, 1]]
visited = set()
q = Queue()

visited.add((1, 1))
q.put((1, 1, 0))


while not q.empty():
    x, y, d = q.get()

    if (x, y) == (31, 39):
        print("solution a: ", d)
        break

    for (dx, dy) in dirs:
        X = x + dx
        Y = y + dy

        if (X, Y) not in visited:
            if is_open(X, Y):
                visited.add((X, Y))
                q.put((X, Y, d+1))

#b)
visited = set()
q = Queue()

visited.add((1, 1))
q.put((1, 1, 0))

while not q.empty():
    x, y, d = q.get()

    if d >= 50:
        print("solution b: ", len(visited))
        break

    for (dx, dy) in dirs:
        X = x + dx
        Y = y + dy

        if (X, Y) not in visited:
            if is_open(X, Y):
                visited.add((X, Y))
                q.put((X, Y, d+1))