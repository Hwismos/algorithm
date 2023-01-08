n, m = map(int, input().split())
data = list(map(int, input().split()))

count = 0
'''
# 무게가 다르면 count 증가
# O(1,000,000) → O(N^2)
for i in range(len(data) - 1):                                  # 마지막 원소를 제외한 수만큼 반복
    for j in range(len(data[i+1:])):                            # i+1 이후의 원소들에 대한 검사 반복
        if data[i] != data[i+j+1]:                              # j가 0부터 시작하기 때문
            # print(f'({data[i]}, {data[i+j+1]})', end='  ')    # 조합 확인
            count += 1
print(f'\n{count}')
'''

# O(1000) → O(N)
array = [0] * 11            # 1부터 10까지 무게를 담는 리스트
for x in data:
    array[x] += 1           # 특정 무게의 볼링공 개수 카운팅

for i in range(1, m+1):
    n -= array[i]           # 전체 볼링공의 개수에서 무게가 i인 볼링공의 개수를 차감
    count += array[i] * n   # 무게가 i인 볼링공의 개수 x i보다 큰 무게를 갖는 볼링공의 개수
print(count)


