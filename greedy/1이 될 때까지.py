N, K = map(int, input().split())

count = 0

'''
# n이 10억, 100억 이상으로 올라가면 1씩 빼는 연산의 수를 매번 진행할 수 없음
# n이 k의 배수가 되도록 효율적으로 한 번에 빼도록 구상
while N != 1:
    if N % K == 0:
        count += 1
        N = N / K
    else:
        count += 1
        N = N - 1
'''

while True:
    # K의 배수인 target을 설정
    target = (N // K) * K
    # N과 target과의 차이만큼 1씩 빼줌
    count += (N - target)   # 이 라인 덕분에 N을 target으로 설정할 수 있게 됨
    N = target      # 이 부분이 빠졌었음
    if N < K:
        break
    count += 1
    N //= K
# N이 K보다 작아져 while문을 탈출했을 때, 1이 되기까지 1을 빼줘야하는 횟수를 계산
count += (N-1)
print(count)

'''
24 5
target은 20
초기 count는 4
20 -> 4
count 1 증가, count는 5
n이 k보다 작아지므로 4를 1까지 줄임
count에 3을 더함
그러면 8?
'''

