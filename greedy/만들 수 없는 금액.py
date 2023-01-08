n = int(input())
data = list(map(int, input().split()))

'''
# 수학적인 성질
- target을 1로 초기화
- target에 포인팅하고 있는 원소를 더해서 업데이트
    - 업데이트된 target값은 첫 원소부터 포인팅하고 있는 원소까지에 해당하는 리스트 내부의 조합으로 (target-1)까지의 순차적인 양수를 만들 수 있음을 의미함
- 모든 원소를 누적한 target이 생성되됐을 때, 전체 리스트의 원소들을 이용해 1부터 (target-1)까지는 만들 수 있지만 target은 만들 수 없음
- 반대로 중간에 target보다 큰 원소값이 나오면 target을 만들 수 없기 때문에 for문 종료
    - (target-1)까지만 가능  
- 위 과정은 오름차순으로 정렬된 리스트에 한해서만 성립함 
'''

'''
리스트: [1, 2, 3]
target      조합
    1(★)     1
    2(★)     2
    3        3
    4(★)     1+3
    5        2+3
    6        1+2+3
    7(★)     X        
'''
data.sort()
target = 1
for x in data:
    if target < x:
        break
    target += x
print(target)

'''
# 오답노트
- l5 ~ l11까지의 주석 내용에 해당하는 수학적 지식이 없었기 때문에 풀지 못한 것
data.sort(reverse=True)
target = 1              # 만들 수 있는지 확인할 금액 변수
while True:
    for coin in data:
        if target > coin:
            continue
        elif target == coin:
            diff = 0
            break
        diff = target - coin
        if diff == 0:
            break
    if diff == 0:
        target += 1
    else:
        break
print(target)
'''
