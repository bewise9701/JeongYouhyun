# if 문
'''
x = 100
if x > 1:
    print("x는 1보다 큽니다.")
'''          
'''
score = int(input("점수를 입력하세요: "))
if score >= 90:
    print("축하합니다.\n합격입니다.\n장학금도 받을 수 있습니다.")# if 문 조건 안에 들여쓰기를 하지 않으면 오류가 발생함.
'''

#else: if 조건을 제외한 모든 경우에 할당됨.
'''
score = int(input("점수를 입력하세요: "))
if score >= 90:
    print("합격입니다.\n장학금도 수령하세요.")
else:
    print('불합격입니다.')

'''
# if는 중첩하여 사용 가능하다.
'''
num = int(input("정수를 입력하세요: "))
if num < 0:
    print("음수입니다.")
else:
    print("양수입니다.")
    if num % 2 == 0:
        print("짝수입니다.")
    else:
        print("홀수입니다.")

'''
# else 외에 elif를 통해서 추가적인 조건을 적어줄 수 있다.
'''
game_score = int(input("점수를 입력하세요: "))
if game_score >= 10000:
    print("고수입니다.")
elif game_score >= 5000:
    print("중수입니다.")
else:
    print("입문자입니다.")
'''
# 입력 숫자를 이용하여 turtle 이용하기
'''
import turtle
t = turtle.Turtle()
t.shape("turtle")

t.penup() # 펜을 올려 그림이 그려지지 않게 함(설정을 안하면 선이 표시됨.)

ti = turtle.textinput("", "숫자를 입력하시오")
n = int(tb)
if n > 0:
    t.goto(100, 100)
    t.write("거북이가 여기로 오면 양수입니다.")
if n == 0:
    t.goto(100, 0)
    t.write("거북이가 여기로 오면 0입니다.")
if n < 0:
    t.goto(100, -100)
    t.write("거북이가 여기로 오면 음수입니다.")
t.goto(0, 0)
t.pendown()
turtle.done()
'''

#도전문제 4.4
'''
import turtle
t = turtle.Turtle()
t.shape("turtle")

t.penup()
x, y = int(turtle.textinput("", "첫번째 숫자를 입력하세요")), int(turtle.textinput("", "두번째 숫자를 입력하세요"))
t.goto(100, 100)
t.write("두 수 모두 양수")
t.goto(100, -100)
t.write("첫번째 수만 양수")
t.goto(-100, 100)
t.write("두번째 수만 양수")
t.goto(-100, -100)
t.write("두 수 모두 음수")
t.goto(0,0)
t.pendown()

if x > 0:
    if y > 0 :
        t.goto(100, 100)
    if y < 0:
        t.goto(100, -100)
if x < 0:
    if y > 0:
        t.goto(-100, 100)
    if y < 0:
        t.goto(-100, -100)
    
'''
#도전문제 4.5
'''
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.penup()

t.goto(100, 0)
t.write("x가 더 큰 수.")
t.goto(-100, 0)
t.write("y가 더 큰 수.")
t.goto(0, 100)
t.write("크기가 같다.")
t.goto(0, 0)

x, y = int(turtle.textinput("", "첫번째 숫자를 입력하세요")), int(turtle.textinput("", "두번째 숫자를 입력하세요"))

if x > y:
    t.goto(100, 0)
elif x < y:
    t.goto(-100, 0)
else:
    t.goto(0, 100)
turtle.done
'''

# 거북이 제어하기 4-3
'''
import turtle
t = turtle.Turtle()
t.shape("turtle")

t.width(3)
t.shapesize(3, 3)

while True:
    command = input("명령을 입력하세요.")
    if command == 'l':
        t.left(90)
        t.forward(100)
    if command == 'r':
        t.right(90)
        t.forward(100)
        
# 도전문제 4.7
    if command == 'f':
        t.forward(100)
'''

# 4-4
'''
year = int(input("연도를 입력해주세요"))
if  (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, "년은 윤년입니다.")
    
else:
    print(year, "년은 윤년이 아닙니다.")
'''

# 4-5
'''
import random

print("동전던지기 게임을 시작합니다.")

coin = random.randrange(2)

if coin == 1:
    print("앞면입니다.")
else:
    print("뒷면입니다.")

print("게임이 종료되었습니다.")
'''

# 4-6
'''
x, y = map(float, input("점의 좌표x, y를 입력하세요:").split())
if x*x + y*y > 5*5:
    print('원 외부에 있음')
else:
    print('원 내부에 있음')
'''

# 도전문제 4.10
'''
x, y = map(float, input("점의 좌표x, y를 입력하세요:").split())
if (x-3) ** 2 + (y-4) ** 2 > 10*10:
    print('원 외부에 있음')
else:
    print('원 내부에 있음')
'''

#도전문제 4.11
'''
id = input("아이디를 입력하세요.")
password = input("비밀번호를 입력하세요.")

if id == "ilovepython" and password == "mypass1234":
    print("환영합니다.")
elif id != "ilovepython":
    print("아이디를 찾을 수 없습니다.")
elif password != "mypass1234":
    print("비밀번호가 틀렸습니다.")
'''
'''
import turtle
t = turtle.Turtle()
t.shape('turtle')
n = int(input("몇 각형을 그리시겠어요?(3~6): "))
for i in range(n):
        t.forward(100)
        t.left(360//n)

turtle.done()


#화씨를 섭씨로, 섭씨를 화씨로 변경하기

fahrenheit = float(input("화씨온도 : "))
celsius = (fahrenheit - 32.0) * 5.0 / 9.0
print("섭씨온도 :", celsius)


#BMI 계산하기
weight = float(input("몸무게를 kg 단위로 입력하시오: "))
height = float(input("키를 m 단위로 입력하시오: "))
bmi = (weight / (height **2))
print("당신의 BMI: ", bmi)

#상대적 지방 질량(RFM) - 내가 한 것

gender = int(input("여성이면 1, 남성이면 0을 입력하세요: "))
height = int(input("당신의 키는 얼마입니까? "))
waist = int(input("당신의 허리둘레는 얼마입니까? "))
rfm_w = 76 - (20 * (height / waist))
rfm_m = 64 - (20 * (height / waist))
if gender == 1:
    print("당신의 RFM은 ", rfm_w)
elif gender == 0:
    print("당신의 RFM은 ", rfm_m)

#상대적 지방 질량(RFM)

gender = int(input("여성이면 1, 남성이면 0을 입력하세요: "))
height = int(input("당신의 키는 얼마입니까? "))
waist = int(input("당신의 허리둘레는 얼마입니까? "))

rfm = 64 - (20 * (height / waist)) + (12 * gender)

print("당신의 RFM은 ", rfm)


# 자동판매기(물건 값은 100단위, 판매기에 500원과 100원 짜리 동전만 있다.)
money = int(input("투입한 돈: "))
price = int(input("물건값: "))
change = money - price
coin_500 = change // 500
coin_100 = (change % 500) // 100
print("투입한 돈:", money, "\n물건값:", price, "\n거스름돈:", change ,"\n500원 동전의 개수:", coin_500, "\n100원 동전의 개수:", coin_100)
'''

# 복합 할당 연산자(산술 연산자와 할당연산자를 결합)
#'a @= b' 는 'a @ b'로 계산된다.

'''
a += b : a + b
a -= b : a - b
a *= b : a * b
a /= b : a / b 등...

# 예시
num = 200
num /= 100
print(num)
'''

# 비교 연산자(두 값의 크기를 비교함)
'''
비교 연산자는 띄어 쓰지 않는다.
등호의 경우, 비교연산자의 위치를 뒤집으면 안된다.
<= (O) , =< (X)

== : 두 값이 같음
!= : 두 값이 다름
> : 좌항이 크다
< : 우항이 크다
>= : 좌항이 같거나 크다


a, b = 100, 200
a == b
'''

# 논리 연산자
'''
bool : 0 이 공란이 아니면 True이고, 0이거나 None, 공란이면 False로 출력된다.
None : 없는 값이라는 의미로, 공란을 표시한다. 0이나 False와는 완전히 다른 의미이므로 주의가 필요함.

* and ,or, not
1) and : 둘 다 참이어야 참
2) or : 둘 중 하나가 참이면 참
3) not : True / False 가 역전됨(논리값이 False면 True)

x = int(input("첫번째 수를 입력하시오: "))
y = int(input("두번째 수를 입력하시오: "))
z = int(input("세번째 수를 입력하시오: "))

avg = (x + y + z) / 3

print("평균 = ", avg)
'''
# map 함수
'''
x, y, z = map(int, input("세 정수를 입력하세요: ").split())
print(x, y, z)
'''
#split
'''
a = "10 20 30"
print(a.split())
= list로 변환됨.
'''
# random 모듈
'''
import random
random.random()
random.randint(1, 10) # 1이상 10 이하
random.randrange(10) #0 이상 10 이하
random.randrange(1, 10) # 1이상 10 미만
random.randrange(0, 10, 2) # 0, 2, 4, 6, 8 중 하나를 반환(10 미만 범위이므로 10 포함 안함, 세번째 수는 간격을 의미함: 2이므로 2 간격으로 작동)

lst = [10, 20, 30, 40, 50]
random.shuffle(lst) # list lst 의 순서를 무작위로 바꿈
random.choice(lst) # list lst의 원소 중 하나를 무작위로 선정함.
'''
# math 모듈
'''
import math
math.pow(3, 3) # 3의 3 제곱(power)
math.fabs(-99) # 실수의 절대값(absolute)
math.log(2.71828)
math.log(100, 10) # 10을 밑으로 하는 100의 로그값
math.pi # 원주율
math.sin(math.pi / 2.0) # 삼각함수 sin
'''





