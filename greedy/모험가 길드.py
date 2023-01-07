n = int(input())
data = list(map(int, input().split()))

data.sort()
guild = []                  # 모험을 떠날 길드
count = 0

# O(N)이므로 O(100,000)
for user in data:
    fear = user             # 유저의 공포도를 저장
    guild.append(user)      # 길드 모집
    # 길드의 인원 수가 유저의 공포도와 같아지면, 해당 길드는 모험을 떠남
    # if len(guild) == fear:
    if len(guild) >= fear:  # 길드의 인원 수가 공포도보다 크더라도 여행을 떠날 수 있음
        count += 1
        guild = []

print(count)