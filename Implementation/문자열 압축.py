INF = 123456789


def encode(s, u):
    result = ''

    # 첫 압축 유닛 설정
    i = 0
    target = s[i: i + u]
    i = i + u
    count = 1

    # 비교 횟수 제한
    for _ in range(1, len(s) // u):
        # 압축 유닛과 현재 덩어리 비교
        if target == s[i: i + u]:
            count += 1
        # result에 추가
        else:
            if count != 1:
                result += (str(count) + target)
            else:
                result += target
            count = 1
            target = s[i: i + u]
        i += u

    # result에 추가되지 않은 덩어리들을 별도로 추가
    if count != 1:
        result += str(count)
    # l26 역행
    result += ''.join(s[i-u:])

    return len(result)


def solution(s):
    result = INF

    if len(s) == 1:
        return 1

    # 압축의 단위 길이
    for unit_len in range(1, len(s) // 2 + 1):
        result = min(result, encode(s, unit_len))
    return result


def main():
    s = "xababcdcdababcdcd"

    '''
    "aabbaccc"	7
    "ababcdcdababcdcd"	9
    "abcabcdede"	8
    "abcabcabcabcdededededede"	14
    "xababcdcdababcdcd"	17
    '''

    print(solution(s))


if __name__ == "__main__":
    main()
