data = list(map(int, list(input())))

# 문자열 길이가 1일 때는 바로 프린트
if len(data) == 1:
    print(data[0])
else:
    data.sort()
    n1 = data[0]
    for n2 in data[1:]:
        # n1과 n2 중 하나라도 0 또는 1이라면 새로운 n1은 n1과 n2의 합 → 1 이하인 경우
        if (0 in [n1, n2]) or (1 in [n1, n2]):
            n1 = (n1 + n2)
        else:
            n1 = (n1 * n2)
    print(n1)
