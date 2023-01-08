# 인자로 전달받은 데이터는 수정 금지
# 수정할 때는 새로운 변수를 할당하고, 이 변수에 연산 값을 저장

from heapq import heappush, heappop


def solution(food_times, k):
    # 모든 음식들의 시간을 다 더한 것보다 k가 크거나 같은 경우
    # 음식들을 다 먹은 뒤 프로그램이 다운됨
    if sum(food_times) <= k:
        return -1

    q = []      # 힙 리스트
    for i in range(len(food_times)):
        heappush(q, (food_times[i], i + 1))  # 힙 생성

    sum_value = 0  # 지금까지 먹기 위해 사용해온 시간
    previous = 0  # 직전에 다 먹은 음식 시간
    length = len(food_times)  # 남은 음식의 개수 (힙의 길이)

    # 지금까지 먹기 위해 사용해온 시간 + (지금 가장 시간이 덜 걸리는 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k를 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        # 지금 시점에서 가장 시간이 덜 걸리는 음식 추출
        now = heappop(q)[0]

        # 가장 시간이 덜 걸리는 음식에서 이전에 먹었던 만큼을 제외하고 남은 시간만큼을, 남은 음식들에 할당
        # 음식을 먹는데 사용한 모든 시간들을 기록
        sum_value += (now - previous) * length

        # 다 먹은 음식을 힙에서 제외
        # 이전에 먹었던 음식의 시간으로, 지금 힙에서 추출한 노드의 음식 시간을 커버할 수 있다면
        # l26에서는 0이 누적됨
        length -= 1

        # 이전 음식 시간 재설정
        # 힙에 저장된 노드의 음식 시간 값은 변경되지 않았음 → previous를 누적해줄 필요가 없는 이유
        # 따라서 직전 노드의 음식을 다 먹었다면, 직전 노드의 음식을 먹는데 걸린 시간만큼을 현재 노드의 시간에서 빼줄 수 있음
        previous = now

    # 남은 음식 중 다음으로 먹어야할 음식이 몇 번째 음식인지 확인
    result = sorted(q, key=lambda x: x[1])
    # k초에서 지금까지 음식을 먹는데 소비한 시간을 차감하고 남은 음식의 개수로 모듈러 연산
    # 결과값(인덱스)에 해당하는 음식이 k초 후에 먹을 음식
    return result[(k - sum_value) % length][1]


print(solution([6, 4, 8], 15))
