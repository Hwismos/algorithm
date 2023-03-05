n = int(input())
arr = list(map(int, input().split()))

d = {}
for idx, num in enumerate(arr):
    d[idx] = num

d = dict(sorted(d.items(), key=lambda item: (item[1], item[0])))

idx = 0
for key, _ in d.items():
    d[key] = idx
    idx += 1

d = dict(sorted(d.items(), key=lambda item: (item[0], item[0])))
for val in list(d.values()):
    print(val, end = ' ')
