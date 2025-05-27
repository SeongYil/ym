import random # 8번 문제 '숫자 맞추기 게임'에서 사용합니다.

# 1. [자릿수 합계]
# 세 자리 정수를 입력받아 각 자릿수의 합을 계산하여 출력하는 프로그램을 작성하세요.
# 힌트: / 연산 후 int()로 정수 몫을 얻고, % 연산자를 활용하세요.
# 예시 입력: 123
# 예시 출력: 6 (1 + 2 + 3)
# --- 답안 코드 ---
num = int(input("세 자리 정수를 입력하세요: "))

hundred = int(num / 100)
ten = int((num % 100) / 10)
one = num % 10

digit_sum = hundred + ten + one
print(digit_sum)
# --- 답안 코드 ---


# 2. [시간 계산]
# 초 단위의 시간을 입력받아, 시, 분, 초로 변환하여 출력하는 프로그램을 작성하세요.
# 힌트: 1시간 = 3600초, 1분 = 60초임을 이용하세요. / 연산 후 int()로 정수 몫을 얻고, % 연산자를 조합하여 사용하세요.
# 예시 입력: 3665
# 예시 출력: 1시간 1분 5초
# --- 답안 코드 ---
total_seconds = int(input("초를 입력하세요: "))

hours = int(total_seconds / 3600)
remaining_seconds = total_seconds % 3600

minutes = int(remaining_seconds / 60)
seconds = remaining_seconds % 60

print(str(hours) + "시간 " + str(minutes) + "분 " + str(seconds) + "초")
# --- 답안 코드 ---


# 3. [최대값 찾기]
# 5개의 정수를 연속적으로 입력받아, 이 중에서 가장 큰 수를 찾아 출력하는 프로그램을 작성하세요.
# 힌트: 현재까지의 최대값을 저장할 변수를 하나 만들고, 입력받은 값과 비교하며 갱신하세요. 반복문(while)을 5번 실행하도록 만드세요.
# 예시 입력: 10, 3, 25, 8, 15
# 예시 출력: 가장 큰 수는 25입니다.
# --- 답안 코드 ---
max_num = 0
count = 0

while count < 5:
    num = int(input(str(count + 1) + "번째 정수를 입력하세요: "))
    if count == 0: # 첫 번째 숫자일 때 max_num을 초기화
        max_num = num
    elif num > max_num:
        max_num = num
    count += 1

print("가장 큰 수는 " + str(max_num) + "입니다.")
# --- 답안 코드 ---


# 4. [평균 계산 (종료 조건)]
# 사용자가 -1을 입력할 때까지 계속해서 점수를 입력받고, -1이 입력되면 그동안 입력된 점수들의 평균을 계산하여 출력하는 프로그램을 작성하세요.
# (단, -1은 평균 계산에 포함하지 않습니다.)
# 힌트: 점수들의 합계와 점수들의 개수를 각각 저장할 변수가 필요합니다. 0으로 나누는 오류를 방지하기 위해 개수가 0인지 확인하세요.
# 예시 입력: 90, 80, 70, -1
# 예시 출력: 평균은 80.0입니다.
# --- 답안 코드 ---
total_score = 0
count = 0

while True:
    score = int(input("점수를 입력하세요 (-1 입력 시 종료): "))
    if score == -1:
        break
    total_score += score
    count += 1

if count > 0:
    average = total_score / count
    print("평균은 " + str(average) + "입니다.")
else:
    print("입력된 점수가 없습니다.")
# --- 답안 코드 ---


# 5. [약수 구하기]
# 정수 하나를 입력받아, 그 수의 모든 약수를 출력하는 프로그램을 작성하세요.
# 힌트: 1부터 입력받은 수까지 반복하면서, 나머지가 0인지 확인하세요.
# 예시 입력: 12
# 예시 출력: 1, 2, 3, 4, 6, 12 (줄 바꿈하여 출력해도 무방)
# --- 답안 코드 ---
num = int(input("정수를 입력하세요: "))

divisor = 1
print(str(num) + "의 약수:")
while divisor <= num:
    if num % divisor == 0:
        print(divisor)
    divisor += 1
# --- 답안 코드 ---


# 6. [소수 판별]
# 정수 하나를 입력받아, 이 수가 소수(1과 자기 자신만으로 나누어 떨어지는 수)인지 아닌지 판별하여 출력하는 프로그램을 작성하세요.
# (1은 소수가 아닙니다.)
# 힌트: 2부터 (입력받은 수 - 1)까지 반복하면서 나누어 떨어지는지 확인합니다. 'is_prime'과 같은 boolean 변수를 활용하면 좋습니다.
# 예시 입력 1: 7 -> 7은(는) 소수입니다.
# 예시 입력 2: 9 -> 9은(는) 소수가 아닙니다.
# --- 답안 코드 ---
num = int(input("정수를 입력하세요: "))

is_prime = True
if num < 2:
    is_prime = False
else:
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            is_prime = False
            break
        divisor += 1

if is_prime:
    print(str(num) + "은(는) 소수입니다.")
else:
    print(str(num) + "은(는) 소수가 아닙니다.")
# --- 답안 코드 ---


# 7. [구구단 출력]
# 사용자로부터 2단부터 9단까지의 숫자를 하나 입력받아, 해당 단의 구구단을 1부터 9까지 곱한 결과를 출력하는 프로그램을 작성하세요.
# 힌트: 입력받은 단에 1부터 9까지의 숫자를 순서대로 곱해보세요. 반복문(while)을 사용하세요.
# 예시 입력: 7
# 예시 출력:
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 9 = 63
# --- 답안 코드 ---
dan = int(input("구구단을 출력할 단을 입력하세요 (2~9): "))

if dan < 2 or dan > 9:
    print("2에서 9 사이의 단을 입력해주세요.")
else:
    multiplier = 1
    while multiplier <= 9:
        result = dan * multiplier
        print(str(dan) + " x " + str(multiplier) + " = " + str(result))
        multiplier += 1
# --- 답안 코드 ---


# 8. [숫자 맞추기 게임]
# 컴퓨터가 1부터 100 사이의 임의의 숫자를 하나 선택하고, 사용자가 이 숫자를 맞출 때까지 계속해서 숫자를 입력받는 게임을 만드세요.
# 사용자가 입력한 숫자가 정답보다 크면 "너무 큽니다!", 작으면 "너무 작습니다!"라고 힌트를 주고,
# 맞추면 "정답입니다! [시도 횟수]번 만에 맞추셨습니다!"를 출력하고 게임을 종료합니다.
# 힌트: import random을 사용하여 random.randint(1, 100)으로 임의의 숫자를 생성할 수 있습니다. 시도 횟수를 셀 변수를 만드세요.
# 예시 (랜덤 숫자가 50일 때):
# 숫자를 맞춰보세요 (1-100): 70 -> 너무 큽니다!
# 숫자를 맞춰보세요 (1-100): 30 -> 너무 작습니다!
# 숫자를 맞춰보세요 (1-100): 50 -> 정답입니다! 3번 만에 맞추셨습니다!
# --- 답안 코드 ---
secret_number = random.randint(1, 100)
attempts = 0

print("1부터 100 사이의 숫자를 맞춰보세요!")

while True:
    try:
        guess = int(input("숫자를 입력하세요: "))
    except ValueError:
        print("유효한 숫자를 입력해주세요.")
        continue

    attempts += 1

    if guess < secret_number:
        print("너무 작습니다!")
    elif guess > secret_number:
        print("너무 큽니다!")
    else:
        print("정답입니다! " + str(attempts) + "번 만에 맞추셨습니다!")
        break
# --- 답안 코드 ---


# 9. [팩토리얼 계산]
# 양의 정수 n을 입력받아, n 팩토리얼(n!)을 계산하여 출력하는 프로그램을 작성하세요.
# (n! = n x (n-1) x ... x 2 x 1, 단 0! = 1)
# 힌트: 결과를 저장할 변수를 1로 초기화하고, 반복문을 돌면서 숫자를 곱해나가세요.
# 예시 입력: 5
# 예시 출력: 120 (5 * 4 * 3 * 2 * 1)
# --- 답안 코드 ---
n = int(input("정수를 입력하세요: "))

factorial = 1
if n < 0:
    print("음수는 팩토리얼을 계산할 수 없습니다.")
elif n == 0:
    print("0!은 1입니다.")
else:
    count = 1
    while count <= n:
        factorial = factorial * count
        count += 1
    print(str(n) + "!은 " + str(factorial) + "입니다.")
# --- 답안 코드 ---


# 10. [거스름돈 계산]
# 물건 가격과 지불한 금액을 입력받아, 거스름돈을 계산하고
# 50000원, 10000원, 5000원, 1000원, 500원, 100원, 50원, 10원 단위로 각각 몇 개의 동전/지폐가 필요한지 출력하는 프로그램을 작성하세요.
# (거스름돈이 부족하거나 딱 맞으면 해당 메시지를 출력)
# 힌트: 각 지폐/동전 단위로 나눗셈(/)을 한 후 int()로 몫을 구하고, 그 나머지를 % 연산자로 다음 단위 계산에 사용하세요.
# 예시 입력: 물건 가격: 17850, 지불한 금액: 20000
# 예시 출력:
# 거스름돈: 2150원
# 1000원: 2개
# 100원: 1개
# 50원: 1개
# --- 답안 코드 ---
price = int(input("물건 가격을 입력하세요: "))
paid_amount = int(input("지불한 금액을 입력하세요: "))

change = paid_amount - price

if change < 0:
    print("금액이 부족합니다.")
elif change == 0:
    print("거스름돈이 없습니다.")
else:
    print("거스름돈: " + str(change) + "원")

    # 50000원
    num_50000 = int(change / 50000)
    if num_50000 > 0:
        print("50000원: " + str(num_50000) + "개")
    change %= 50000

    # 10000원
    num_10000 = int(change / 10000)
    if num_10000 > 0:
        print("10000원: " + str(num_10000) + "개")
    change %= 10000

    # 5000원
    num_5000 = int(change / 5000)
    if num_5000 > 0:
        print("5000원: " + str(num_5000) + "개")
    change %= 5000

    # 1000원
    num_1000 = int(change / 1000)
    if num_1000 > 0:
        print("1000원: " + str(num_1000) + "개")
    change %= 1000

    # 500원
    num_500 = int(change / 500)
    if num_500 > 0:
        print("500원: " + str(num_500) + "개")
    change %= 500

    # 100원
    num_100 = int(change / 100)
    if num_100 > 0:
        print("100원: " + str(num_100) + "개")
    change %= 100

    # 50원
    num_50 = int(change / 50)
    if num_50 > 0:
        print("50원: " + str(num_50) + "개")
    change %= 50

    # 10원
    num_10 = int(change / 10)
    if num_10 > 0:
        print("10원: " + str(num_10) + "개")
# --- 답안 코드 ---