def flip(s):
    count_0, count_1 = 0, 0         # 모두 0 혹은 1로 바꿀 때의 뒤집기 횟수 초기화

    if s[0] == 1:
        count_0 += 1                # 첫 수가 1이면 0으로 바꿔야 하는 카운트가 1 증가
    else:
        count_1 += 1

    for i in range(len(s) - 1):
        if s[i] != s[i+1]:          # (★)현재 포인팅하고 있는 수와 그 다음의 수가 다를 경우
            if s[i+1] == 0:         # i+1번째 수가 0이라면 모든 문자를 1로 바꿔야 하는 카운트 변수를 1 증가
                count_1 += 1
            else:
                count_0 += 1
    return min(count_1, count_0)
def main():
    s = list(map(int, list(input())))
    print(flip(s))

# 해당 파일 자체를 실행하는 경우와 다른 모듈에서 이 모듈을 임포트해서 사용할 때를 구분하기 위함
    # 다른 모듈에서 이 모듈을 임포트할 때는 main이 아닌 다른 메소드만을 이용하고자 할 수 있음
# 해당 파일(모듈) 자체를 실행하는 경우에는 main 메소드를 호출하도록 강제하기 위함
if __name__ == '__main__':
    main()
