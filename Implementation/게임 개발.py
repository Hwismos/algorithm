n, m = map(int, input().split())
x, y, direction = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

d = [[0] * m for _ in range(n)]
d[x][y] = 1  # 현재 좌표 방문 처리

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 왼쪽으로 회전
# change_direction
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


##########################################################################


def change_direction():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def set_new_position(row, col):
    new_x = row + moves[direction][0]
    new_y = col + moves[direction][1]

    return new_x, new_y


def set_past_position(row, col):
    new_x = row - moves[direction][0]
    new_y = col - moves[direction][1]

    return new_x, new_y


def update_position(new_pos):
    global x, y
    x, y = new_pos[0], new_pos[1]


def is_sea(new_pos):
    if data[new_pos[0]][new_pos[1]] == 1:
        return True
    return False


def has_gone_before(new_pos):
    if d[new_pos[0]][new_pos[1]] == 1:
        return True
    return False


def log_visited(new_pos):
    d[new_pos[0]][new_pos[1]] = 1


# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # change_direction
    # turn_left()
    change_direction()

    # make_move
    # nx = x + dx[direction]
    # ny = y + dy[direction]
    nx, ny = set_new_position(x, y)

    # 회전한 이후 정면에 가보지 않은 칸이 있는 경우 이동
    # 가보지 않았고 육지여야 함
    # if d[nx][ny] == 0 and data[nx][ny] == 0:
    if not (has_gone_before((nx, ny))) and not (is_sea((nx, ny))):
        # 방문 기록
        # d[nx][ny] = 1
        log_visited((nx, ny))

        # 위치 갱신
        # x = nx
        # y = ny
        update_position((nx, ny))
        count += 1

        turn_time = 0   # reset_turn_time()
        continue
    # 회전 이후 모두 가본 칸이거나 바다
    else:
        turn_time += 1      # increase_turn_time()
    if turn_time == 4:      # if check_all_directions():
        # nx = x - dx[direction]
        # ny = y - dy[direction]
        nx, ny = set_past_position(x, y)
        # print(f'방향: {direction}, ({x}, {y}), ({nx}, {ny})')

        # make_move_back
        # if data[nx][ny] == 0:
        if not (is_sea((nx, ny))):
            # x = nx
            # y = ny
            update_position((nx, ny))
        # if is_sea():
        else:
            break
        turn_time = 0       # reset_turn_time()
print(count)

# 방문 위치 확인
for i in range(len(d)):
    print(d[i])
