N, M = map(int, input().split())
data = []
first_col = []
for row in range(N):
    # 행 데이터를 받으며 바로 정렬
    # 이때는 O(log(10000))의 시간이 걸림
    # min 함수를 사용할 수도 있음
    data.append(sorted(list(map(int, input().split()))))
    # 각 행의 최소 값들로만 이루어진 리스트를 생성
    first_col.append(data[row][0])

# N이 100이하기 때문에 O(log(100))
first_col.sort(reverse=True)
print(first_col[0])



