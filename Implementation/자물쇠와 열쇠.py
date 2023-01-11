# 고려 사항
# 경계 지점 고려

def print_matrix(data):
    for line in data:
        print(line)
    print('\n')


def make_lock_bigger(key, lock):
    m = len(key)
    n = len(lock)
    x = n + ((m - 1) * 2)
    big_lock = [[0] * x for _ in range(x)]

    for i in range(n):
        for j in range(n):
            big_lock[i + m - 1][j + m - 1] = lock[i][j]
    return big_lock


def copy_matrix(_from, _to):
    for i in range(len(_from)):
        for j in range(len(_from[i])):
            _from[i][j] = _to[i][j]


def is_match(key, big_lock):
    m = len(key)
    n = len(big_lock)
    x = n - ((m - 1) * 2)
    copied_big_lock = [[0] * n for _ in range(n)]
    check_lock = [[0] * x for _ in range(x)]

    copy_matrix(copied_big_lock, big_lock)

    for i in range(n - m + 1):
        for j in range(n - m + 1):
            for x in range(m):
                for y in range(m):
                    copied_big_lock[x + i][y + j] += key[x][y]
            for x in range(m):
                for y in range(m):
                    check_lock[x][y] = copied_big_lock[x + m - 1][y + m - 1]
            for each_line in check_lock:
                if not(all(each_line)):
                    break
            else:
                return True
            copy_matrix(copied_big_lock, big_lock)
    return False


def rotate_key(key):
    """
    (0, 0) -> (0, 2)
    (0, 1) -> (1, 2)
    (0, 2) -> (2, 2)
    (1, 0) -> (0, 1)
    (1, 1) -> (1, 1)
    (1, 2) -> (2, 1)
    (2, 0) -> (0, 0)
    (2, 1) -> (1, 0)
    (2, 2) -> (2, 0)
    """
    m = len(key)
    rotated_key = [[0] * m for _ in range(m)]

    for i in range(m):
        for j in range(m):
            rotated_key[i][j] = key[m - j - 1][i]
    return rotated_key


def solution(key, lock):
    big_lock = make_lock_bigger(key, lock)

    for i in range(4):
        if is_match(key, big_lock):
            return True
        key = rotate_key(key)
    return False


def main():
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    if solution(key, lock):
        print('True')
    else:
        print('False')


if __name__ == "__main__":
    main()
