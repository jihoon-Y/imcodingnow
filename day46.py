# 제어문 02. while 반복문 문법

# while 조건 부분:  <- 불린 값으로 계산되는 식이다 x < 3, name == "지훈" 등
#     수행 부분  <- 반복적으로 실행하고 싶은 명령이다 [출력] print("지훈"), [변수변경] i = i + 1 등
# 조건 부분의 결과값이 True인 동안, 계속해서 수행 부분이 실행되는 구조이다
# 결과값이 False이면 while문에서 나오게 된다

i = 1
while i <= 3:
    print("나는 지훈이다!")
    i += 1


# 제어문 03. while 반복문 실습 1
# while 반복문을 사용하여 1 이상 100 이하의 짝수를 모두 출력하자

i = 2
while i <= 100:
    print(i)
    i += 2