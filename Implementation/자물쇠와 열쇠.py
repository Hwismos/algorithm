def rotate_key(key):
    m = len(key)
    rotated_key = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            rotated_key[j][m - i - 1] = key[i][j]
    return rotated_key


def check(new_lock):
    m = len(new_lock) // 3

    for i in range(m, 2*m):
        for j in range(m, 2*m):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)

    # 자물쇠 크기를 기존은 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    # 새로운 자물쇠에 기존 자물쇠 내용 삽입
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotate_key(key)
        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠에 열쇠 삽입
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 새 자물쇠를 이용해 열쇠가 정확한지를 검사
                if check(new_lock):
                    return True
                # 새 자물쇠에서 열쇠 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False
