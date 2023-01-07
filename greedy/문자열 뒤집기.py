# 상수 설정
ONE = 1
ZERO = 0


def flip_to(s, target):
    count = 0
    flag = 0

    if target == ONE:
        to_change = ZERO
    else:
        to_change = ONE

    for elem in s:
        if flag == 0:
            if elem == to_change:
                flag = 1
        if flag == 1:
            if elem == target:
                count += 1
                flag = 0
    return count


def main():
    s = list(map(int, list(input())))
    # print(min(flip_to(s, ONE), flip_to(s, ZERO)))
    print(flip_to(s, ONE))
    print(flip_to(s, ZERO))

# 해당 파일 자체를 실행하는 경우와 다른 모듈에서 이 모듈을 임포트해서 사용할 때를 구분하기 위함
# 해당 파일(모듈) 자체를 실행하는 경우에는 main 메소드를 호출하도록 강제하기 위함
if __name__ == '__main__':
    main()
