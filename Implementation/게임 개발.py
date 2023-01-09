n, m = map(int, input().split())
row, col, direction = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

new_row, new_col = row, col
new_direction = direction


def is_sea():
    # 이동된 위치가 바다면 True 반환
    if data[new_row][new_col] == 1:
        return True
    return False


def has_gone_before():
    # 가본 곳은 2로 표기
    if data[new_row][new_col] == 2:
        return True
    return False


def make_move_back():
    global new_row, new_col     # ?
    new_row = row
    new_col = col

    # data[new_row][new_col] = 0  # ?


def make_move():
    global new_row
    global new_col

    new_row = row + moves[direction][0]
    new_col = col + moves[direction][1]


def change_direction(x):
    if x > 1:
        return x - 1
    # 0이면 3 반환
    else:
        return 3


moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북, 동, 서 ,남

while True:
    print(f'위치: ({new_row}, {new_col})')
    if has_gone_before() or is_sea():  # 이동해온 곳이 이미 가본 칸이거나 바다로 되어 있다면
        make_move_back()  # 뒤로 이동
        if is_sea():    # 뒤로 갔는데 바다면 종료
            break
        data[new_row][new_col] = 0
        continue
    row = new_row
    col = new_col
    data[row][col] = 2
    for i in range(len(moves)):  # 네 방향에 대해
        direction = change_direction(direction)
        make_move()
        break
