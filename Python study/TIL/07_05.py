# 5장

# 리스트를 반복문을 이용하여 원소를 빼낼 수 있다.
'''
for i in [1, 2, 3, 4, 5]:
    print("i = ", i)
'''
# string도 리스트의 일종이므로 for을 적용하여 모든 문자를 출력할 수 있다.
'''
for str in "hello":
    print("i = ", str)
    
'''
# 5.4 for in 다음에는 리스트나 문자열도 올 수 있다(이를 이용해 구구단을 만들 수 있다.)
'''
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print("9 * i = ", 9 * i)
'''
# 5.5 range 함수를 이용하여 for을 만들면 도움이 된다.
'''
L = list(range(10))
print(L)
'''
# range 함수 세분화: range(시작값, 멈추는 값, 숫자의 간격)
'''
for i in range(20, 10, -3):
    print(i, end = " ")     # print에서 end 값은 각 값 사이의 표시자를 나타내준다(이 경우, 줄바꿈이 안됨.)
'''    

# 5 - 1 터틀그래픽으로 여러개 그리기
'''
import turtle
t = turtle.Turtle()
t.shape("turtle")

for i in range(3):
    t.circle(100)
    t.left(360/3)

'''
# 여러개의 도형 그리기
'''
import turtle
t = turtle.Turtle()
t.shape("turtle")

for i in range(3):
    t.forward(100)
    t.left(360/3)
    
t.penup()
t.goto(200,0)
t.pendown()

for i in range(4):
    t.forward(100)
    t.left(360/4)

for i in range(6):
    t.forward(100)
    t.left(360//6)
'''
# 텍스트 상자로 수를 입력받아 이에 해당하는 도형 그리기
'''
import turtle
t = turtle.Turtle()

input_number = int(turtle.textinput("", "몇각형을 원하시나요?"))
for i in range(input_number):
    t.forward(100)
    t.left(360/input_number)
'''
# 거북이가 무작위로 움직이게 하기
'''
import turtle
import random

t = turtle.Turtle()
t.shape("turtle")
lst = [90, 180, 270, 360]

for i in range(50):
    leng = random.randint(1,90)
    angle = random.choice(lst)
    t.forward(leng)
    t.left(angle)
turtle.done()
'''
# 팩토리얼 만들기
'''
n = int(input("정수를 입력하시오: "))
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print(n, "!은", fact, "입니다.")
'''
# while 반복문 만들기
'''
under_construction = True
while under_construction:
    response = input("공사가 완료되었습니까?")
    if response == "y":
        under_construction = False
        
print("End loop")
'''

#패스워드 확인하기

'''
password = ""
while password != "pythonisfun":
    password = input("암호를 입력하세요")
print("로그인 되었습니다.")
'''
# while을 이용하여 도형 그리기
'''
import turtle
t = turtle.Turtle()
i = 0
while i < 4:
    t.forward(100)
    t.right(90)
    i = i + 1
'''
# while을 이용하여 구구단 만들기
# %는 출력 포맷을 이야기 하고, %s 는 문자열을 이야기 한다. %d 는 정수, %f는 float을 가르킨다.
'''
num =2
#for n in range(2, 10, 1):
while num <= 9:
    i = 1
    while i <= 9:
        print("%s * %s = %s" % (num, i, num * i))
        i = i + 1
    print("----------")
    num = num + 1
'''
# 중첩 없이 처리하는 방법
'''
i = 1
while i <= 81:
    if i % 9 == 0:
        print("%s X 9 = %s" % (i//9, i))
        print("-----------")
        print("")
    else:
        print("%s X %s = %s" % (i//9 + 1, i % 9, (i//9 + 1) * (i % 9)))
    i = i + 1
'''
# 별 그리기
'''
import turtle
t = turtle.Turtle()
i = 0
while i < 5:
    t.forward(150)
    t.right(144)
    i = i + 1
'''
# 도전 문제 5.8(2)
'''
import turtle
t = turtle.Turtle()
i = 0
while i < 18:
    t.forward(200)
    t.right(140)
    i = i + 1
'''
# 도전 문제 5.8(3)
'''
import turtle
t = turtle.Turtle()
i = 0

while i < 5:
    t.forward(50)
    t.right(144)
    t.forward(50)
    t.left(72)
    i += 1
'''


# 나선형 도형 만들기
'''
import turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)

i = 10
while i < 500:
    t.forward(i)
    t.right(89)
    i = i + 5
#   i += 5 로 작성해도 된다.
'''
'''
import turtle
t = turtle.Turtle()
t.speed(0)
t.width(3)

i = 10
while i < 500:
    t.forward(i)
    t.right(89)
    i = i + 5
'''
# 입력된 값의 합 계산하기
'''
answer = "yes"
number = 0
while con == "yes":
    number = int(input("숫자를 입력하시오: "))
    answer = input("계속?(yes/no): ")
    total += number
print('합계는 : ', total)
'''

