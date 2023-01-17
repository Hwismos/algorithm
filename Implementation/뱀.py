"""
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
-> 9
"""

from collections import deque

n = int(input())
k = int(input())
apple = []
for _ in range(k):
    apple.append(tuple(map(int, input().split())))
l = int(input())
directions = []
for i in range(l):
    directions.append(input().split())

# initial pos
x = 0
y = 0
tail_pos = deque([(0, 0)])
dir_ = 'D'
time = 0


def is_apple():
    if [new_x, new_y] in apple:
        apple.remove([new_x, new_y])
        return True
    return False


while True:
    # move_head()
    if dir_ == 'D':
        new_x = x
        new_y = y + 1
    else:
        new_x = x + 1
        new_y = y

    if not(0 <= new_x <= n-1 and 0 <= new_y <= n-1) or (new_x, new_y) in tail_pos:
        time += 1
        break

    if not(is_apple()):
        # 몸길이 유지
        tail_pos.pop()
        tail_pos.appendleft((new_x, new_y))

    # time_up()
    time += 1
    # if time_to_change_dir():
    for d in directions:
        if d[0] > time:
            break
        else:
            dir_ = d[0][1]
            directions.pop(0)
    # update pos
    x = new_x
    y = new_y
print(time)