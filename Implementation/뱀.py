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

n = int(input())
k = int(input())
apple = []
for _ in range(k):
    apple.append(tuple(map(int, input().split())))
l = int(input())
directions = []
for _ in range(l):
    directions.append(tuple(map(int, input().split())))

head_pos = [(0, 0)]
tail_pos = [(0, 0)]
dir_ = 'D'
time = 0
while True:
    # get_now_pos
    x, y = head_pos[-1][0], head_pos[-1][1]

    # move_head()
    if dir_ == 'D':
        new_x = x
        new_y = y + 1
    else:
        new_x = x + 1
        new_y = y

    if game_over():
        time += 1
        break

    if is_apple():
        # 몸길이를 늘림
        pass
    else:
        # 몸길이 유지
        pass

    # time_up()
    time += 1
    # if time_to_change_dir():
    for d in directions:
        if d[0] > time:
            break
        else:
            dir_ = d[0][1]
            directions.pop(0)
