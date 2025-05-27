# 2주차 수업 요약

# 조건문

# 반복문


# 조건: 날씨가 맑다면 
# 조건이 참 일 때 할 것 : 소풍을 간다 , 우산을 챙기지 않는다다

#if 만약에 ~~하면 ~~한다 A가 참이면, B를 한다

#컴퓨터와 대화하기 위한 언어들은, 한 줄씩 읽음

# 만약에 날씨가 맑다면 소풍을 간다, 우산을 챙기지 않는다
weather = "맑음"

if weather == "맑음":
    print("소풍을 간다")
    print("우산을 챙기지 않는다")

#if else:

#만약에 날씨가 맑으면 소풍을 간다, 우산을 챙기지 않는다. 날씨가 맑지 않다면! 집콕을 한다

if weather == "맑음":
    print("소풍을 간다")
    print("우산을 챙기지 않는다")
else: 
    print("집콕")


#만약에 나이가 5세 미만은 유아고, 나이가 5이상 20살 미만은 청소년, 그외 사람은 성년

#if elif else:


age = 15
if age < 5:
    print("유아")
elif 5 < age and age < 20 and age != 15:
    print("청소년")
elif age == 15:
    print("중2병")
else:
    print("성년")



#while:

# 0부터 1000까지 더한 값을 알고싶다.

# 0 + 1 + 2 + 3 + 4 + 5 + ....

sum = 0

count = 0

# 순수 구현
# 알고리즘


while count <= 1000:
    sum = sum + count
    count = count + 1

while True:
    print("반복중")

#반복문의 조건은 끝이 나게 코딩을 해야한다!

#예제문제와 답안 그리고, 매뉴얼을 올렸어

#https://www.github.com/SeongYil/python_exercise



