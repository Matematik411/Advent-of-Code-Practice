s = 3001330

circle = {i: i+1 for i in range(s)}
circle[s-1] = 0

player = 0
for _ in range(s-1):
    circle[player] = circle[circle[player]]
    player = circle[player]

print("winner is: ", player+1)

#b)
from collections import deque
#levi in desni deque (zato da lahko hitro jemljem iz obeh strani) glede na player
# TU IMAM 1 --> s
left = deque()
right = deque()
rem = s
for i in range(1, s+1):
    if i <= s // 2:
        left.append(i)
    else:
        right.appendleft(i)

s_left = len(left)
s_right = len(right)

for _ in range(s-1):
    if s_left > s_right:
        left.pop()
        s_left -= 1
    else:
        right.pop()
        s_right -= 1
    rem -= 1

    right.appendleft(left.popleft())
    left.append(right.pop())

print("this time, the winner is: ", left.pop())