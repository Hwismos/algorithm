from heapq import heappush, heappop


def solution(food_times, k):
    h = []  # 힙 자료구조를 위한 변수
    n = len(food_times) # 음식의 개수 변수
    for num, food in enumerate(food_times):
        heappush(h, (food, num+1))

    prev = 0    # 이전 음식을 먹을 때 사용한 시간
    result = []
    while True:
        food = heappop(h)[0]    # 가장 적은 시간이 소비되는 음식 pop
        if food-prev == 0:
            continue
        if k < (food-prev) * n:     # n개의 음식을 모두 한 번씩 섭취할 시간이 가능한지 확인
            n = len(h)
            for _ in range(n):
                result.append(heappop(h))
            break
        k -= (food - prev) * n  # food만큼의 시간이 걸리는 음식들을 모두 섭취
        prev += food    # 음식을 섭취한 시간 누적
    result.sort(key=lambda x: x[1])
    return result[k % len(result)][1]


print(solution([8, 4, 6], 15))
