N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

# 실질적으로 사용하는 수는 가장 큰 수와 그 다음으로 큰 수
first = data[-1]
second = data[-2]
result = 0

# 두 값이 같으면 중복해서 사용할 수 있음
if first == second:
    result = first * M
# 가장 큰 수가 곱해지는 수를 계산해서 N이 커졌을 때의 시간 초과 문제를 해결
else:
    result += (first * K) * (M % K)
    result += (second * (M % K))

print(result)