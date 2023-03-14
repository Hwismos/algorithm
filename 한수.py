n = int(input())

result = 0
if n < 111:
    if n >= 100:
        result = 99
    else:
        result =n
else:
    result = 99
    if n == 111:
        result += 1
    else:
        if n == 1000:
            n = 999
        list_ = [1,1,1]
        int_ = int(''.join(list(map(str, list_))))
        while int_ <= n:
            diff_1 = list_[1] - list_[0]
            diff_2 = list_[2] - list_[1]
            if diff_1 == diff_2:
                result += 1
            
            list_[2] += 1
            if list_[2] == 10:
                list_[2] = 0
                list_[1] += 1
                if list_[1] == 10:
                    list_[1] = 0
                    list_[0] += 1

            int_ = int(''.join(list(map(str, list_))))

print(result)