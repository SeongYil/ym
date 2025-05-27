# 문제 1
# 사용자에게 이름을 입력받고, "안녕하세요, [이름]님!"이라고 출력하세요.
# 힌트: input(), print(), 문자열 연결(+)
name = input("이름을 입력하세요: ")
print("안녕하세요, " + name + "님!")

# 문제 2
# 사용자에게 두 숫자를 입력받고, 더한 값을 출력하세요.
# 힌트: input(), int(), print()
a = int(input("첫 번째 숫자: "))
b = int(input("두 번째 숫자: "))
print("합:", a + b)

# 문제 3
# 사용자에게 나이를 입력받고, 20살 이상이면 "성인입니다.", 아니면 "미성년자입니다."라고 출력하세요.
# 힌트: input(), int(), if-else
age = int(input("나이를 입력하세요: "))
if age >= 20:
    print("성인입니다.")
else:
    print("미성년자입니다.")

# 문제 4
# 사용자에게 숫자를 하나 입력받고, 짝수이면 "짝수입니다." 홀수이면 "홀수입니다."라고 출력하세요.
# 힌트: %, if-else
num = int(input("숫자를 입력하세요: "))
if num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

# 문제 5
# 1부터 10까지 숫자를 출력하세요. (while 사용)
# 힌트: while, 변수 증가
i = 1
while i <= 10:
    print(i)
    i += 1

# 문제 6
# 사용자에게 원하는 단을 입력받아 구구단을 출력하세요. (예: 3단)
# 힌트: input(), int(), while, 변수 증가
dan = int(input("몇 단을 출력할까요? "))
i = 1
while i <= 9:
    print(dan, "x", i, "=", dan * i)
    i += 1

# 문제 7
# 숫자 맞히기 게임을 만드세요.
#   1) 컴퓨터가 1~10 사이의 랜덤 숫자를 하나 정합니다.
#   2) 사용자가 숫자를 입력해 맞힐 때까지 계속 반복합니다.
#   3) 맞히면 "정답입니다!"를 출력하고 게임을 종료합니다.
#
# ── random 모듈 사용법 설명 ─────────────────────────────────────────
#   import random                  # ① random 모듈 불러오기
#   secret = random.randint(1, 10) # ② 1~10 사이 임의 정수 생성
#                                   #    └→ randint(a, b): a 이상 b 이하
#   # 이제 secret 변수에 담긴 숫자를 사용자가 맞히도록 while 문으로 반복!
# ───────────────────────────────────────────────────────────────────
#
# 힌트: import random, random.randint(), while, input(), int(), if‑else
import random
secret = random.randint(1, 10)
guess = 0
while guess != secret:
    guess = int(input("1~10 숫자를 맞혀보세요: "))
    if guess == secret:
        print("정답입니다!")
    else:
        print("틀렸습니다. 다시 시도하세요.")

# 문제 8
# 사용자에게 세 개의 숫자를 입력받고, 가장 큰 수를 출력하세요.
# 힌트: input(), int(), if-elif-else 또는 변수 비교
a = int(input("첫 번째 숫자: "))
b = int(input("두 번째 숫자: "))
c = int(input("세 번째 숫자: "))
max_num = a
if b > max_num:
    max_num = b
if c > max_num:
    max_num = c
print("가장 큰 수는:", max_num)

# 문제 9
# 1부터 100까지의 숫자 중에서 3의 배수만 출력하세요.
# 힌트: while, 변수 증가, %, if
i = 1
while i <= 100:
    if i % 3 == 0:
        print(i)
    i += 1

# 문제 10
# 비밀번호 확인 프로그램을 만드세요.
# 비밀번호를 먼저 설정하고, 사용자가 맞게 입력할 때까지 반복하게 하세요.
# 힌트: input(), while, if
password = input("비밀번호를 설정하세요: ")
guess = ""
while guess != password:
    guess = input("비밀번호를 입력하세요: ")
print("비밀번호가 확인되었습니다.")

# 문제 11
# 팩토리얼을 계산하는 함수를 만들어서,
# 사용자에게 숫자를 입력받고 결과를 출력하세요.
# 힌트: def 함수 정의, while, 곱셈 누적 또는 import math 사용 가능
def factorial(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result

n = int(input("팩토리얼을 계산할 숫자: "))
print(factorial(n))

# 문제 12
# 간단한 계산기를 만드세요. 두 수와 연산자(+,-,*,/)를 입력받고 결과를 출력하세요.
# 힌트: input(), int(), if-elif-else
a = int(input("첫 번째 숫자: "))
op = input("연산자(+,-,*,/): ")
b = int(input("두 번째 숫자: "))
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("알 수 없는 연산자입니다.")

# 문제 13
# "Hello"를 5번 출력하는 함수를 만드세요. (while 사용)
# 힌트: def 함수 정의, while, 변수 증가
def say_hello():
    i = 0
    while i < 5:
        print("Hello")
        i += 1

say_hello()

# 문제 14
# 사용자가 몇 개의 숫자를 입력할 것인지 먼저 입력 받고,
# 그 숫자들을 하나씩 입력받아 모두 더한 값을 출력하세요.
# 힌트: input(), int(), while, 누적합 변수
count = int(input("몇 개의 숫자를 입력할까요? "))
i = 0
total = 0
while i < count:
    num = int(input("숫자를 입력하세요: "))
    total += num
    i += 1
print("총합:", total)

# 문제 15
# 2자리 숫자 비밀번호를 맞히는 업다운 게임을 만드세요.
# 컴퓨터가 만든 비밀번호보다 크면 "다운!", 작으면 "업!" 출력.
# 맞히면 "정답입니다!" 출력
# 힌트: import random, random.randint(), while, if-elif-else
import random
password = random.randint(10, 99)
guess = 0
while guess != password:
    guess = int(input("2자리 비밀번호를 맞혀보세요: "))
    if guess < password:
        print("업!")
    elif guess > password:
        print("다운!")
    else:
        print("정답입니다!")

# 문제 16
# 사용자에게 정수를 입력받고, 그 수가 소수인지 아닌지 출력하세요.
# 힌트: while문으로 2부터 n-1까지 나누어보기, %, if
num = int(input("숫자를 입력하세요: "))
i = 2
is_prime = True
if num < 2:
    is_prime = False
else:
    while i < num:
        if num % i == 0:
            is_prime = False
            break
        i += 1
if is_prime:
    print("소수입니다.")
else:
    print("소수가 아닙니다.")

# 문제 17
# 1부터 100까지의 합을 구하는 프로그램을 만드세요.
# 힌트: while, 누적합 변수, 변수 증가
i = 1
total = 0
while i <= 100:
    total += i
    i += 1
print("1부터 100까지의 합:", total)

# 문제 18
# 가위바위보 게임을 만드세요.
# 사용자와 컴퓨터가 가위(1), 바위(2), 보(3)를 선택하고 결과를 출력하세요.
# 힌트: input(), random.randint(), if-elif-else
import random
user = int(input("가위(1), 바위(2), 보(3) 중 선택하세요: "))
com = random.randint(1, 3)
print("컴퓨터:", com)
if user == com:
    print("비겼습니다.")
elif (user == 1 and com == 3) or (user == 2 and com == 1) or (user == 3 and com == 2):
    print("이겼습니다!")
else:
    print("졌습니다.")
