n = int(input())
INF = 1e9

five_num = 0
three_num = 0
result = INF

while 5 * five_num <= n:
    m = n - 5 * five_num
    three_num = 0
    while 3 * three_num <= m:
        three_num += 1
    three_num -= 1
    if 3 * three_num == m:
        if five_num + three_num < result:
            result = five_num + three_num
    five_num += 1        

if result == INF:
    print(-1)
else:
    print(result)
    