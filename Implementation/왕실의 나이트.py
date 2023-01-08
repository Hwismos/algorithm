s = input()
col, row = s[0], s[1]

# ord(문자): 인자를 문자에 해당하는 아스키코드로 변환
# chr(숫자): 인자를 숫자에 맞는 아스키코드로 변환
row = ord(row) - ord('1')
col = ord(col) - ord('a')

steps = [(-2, 1), (-2, -1), (2, 1), (2, -1), (-1, 2), (1, 2), (-1, -2), (1, -2)]
count = 0

# 인자(row, col) 변경 금지
for step in steps:
    new_row = row + step[0]
    new_col = col + step[1]
    if 0 <= new_row <= 7 and 0 <= new_col <= 7:
        count += 1
print(count)
