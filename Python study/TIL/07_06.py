# 5.9 무한루프와 break로 빠져나가기
'''
while True:
    light = input('신호등 색상을 입력하시오:')
    if light == 'green':
        break
print("전진")
'''
#도전문제 5.12
'''
# 교재 답안
str = input('단어를 입력하세요')
for st in str:
    if st in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        break
    print(st, end ="")

# 리스트를 활용하여 처리하는 방법
str = list(input('단어를 입력하세요'))
for st in str:
    if st in ['a', 'e', 'i', 'o', 'u'] or ['A', 'E', 'I', 'O', 'U']:
        str.remove(st)
        break
    print(st, end = '')
'''
# 5.10 루프를 제어하는 고급 기법: continue와 break
'''
Continue는 조건에 해당되는 경우는 그냥 건너뜀.
Break는 조건에 해당되면 멈춤.
'''
# 5.11 포메팅
'''
'{} Python!'.format('Hello')

print('I like {0} and {1}.'.format('Python', 'Java'))

'소수점 아래 두자리 정밀도 : {0:.2f}, 세자리 정밀도 : {0:.3f}'.format(1/3)
'전체 10칸을 차지하는 실수 : {0:10.3f}, {0:10.4f}'.format(3.1415926)

for i in range(2, 11, 2):
    print('{0:3d} {1:4d} {2:5d}'.format(i, i*i, i*i*i))
'''

#6.2 예약어로 함수 작성하기
'''
def print_address():
    print('경상북도\n울릉군 울릉읍\n독도리 산 1-96번지')
print_address()
'''

#6.1 도전문제
'''
def print_star() :
    print('********************')
print_star()
print_star()
print_star()
print_star()
print_star()

# for loop을 사용하여 하는 방법
def print_star(n) :
    for star in range(int(n)):
        print("*", end="")  # 별마다 줄이 바뀌는 것을 방지
    print()                 # 임의로 공백 설정

print_star(20)
print_star(20)
print_star(20)

def print_address(name):
    print("서울 특별시 종로구 1번지\n파이썬 빌딩 7층\n", name)
print_address(1)
print_address(2)
'''
# 6.6 함수에 여러값을 넣어주기
'''
def get_sum(start, end):
    s = 0
    for i in range(start, end + 1):
        s += i
    return s
x = get_sum(1, 10)
y = get_sum(1, 20)
print('x =', x)
print('y =', y)
'''
# 6.7 여러 개의 값을 넘겨주고 여러 개의 값을 돌려받자
'''
def sort_num(n1, n2):
    if n1 < n2:
        return n1, n2
    else:
        return n2, n1

print(sort_num(110, 210))
print(sort_num(2100, 80))

def get_square(a, b, c):
    a_sq = a ** 2
    b_sq = b ** 2
    c_sq = c ** 2
    return a_sq, b_sq, c_sq

print(get_square(1, 2, 3))
'''
#터틀을 사용하여 다각형 그리기
'''
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

square(100)
square(200)
square(300)

def n_polygon(n, length):
    for i in range(n):
        t.forward(length)
        t.left(360//n)

for i in range(10):
    t.left(20)
    n_polygon(5, 100)
'''
#변수의 범위 찾기
'''
def print_counter():
    print('counter =', counter)
counter = 100
print_counter()

counter = 200
print_counter()
'''

# 6.9 전역변수 사용하기: global
'''
def calculate_area(radius):
    global area
    area = 3.14 * radius ** 2
    return
area = 0
r = float(input("원의 반지름: "))
calculate_area(r)
print(area)
'''
# 6.10 default argument
'''
def order(num, pickle= True, onion = True):
    print('햄버거 {0}개 - 피클 {1}, 양파 {2}'.format(num, pickle, onion))
order(1, pickle = False, onion = True)
order(2)
'''
# 주급 계산 프로그
def weeklyPay(rate, hour):
    
    if hour > 30:
        totalPay = (rate * 30) + rate * 1.5 * (hour - 30)
        
    else:
        totalPay = rate * hour
        
    return totalPay

print(weeklyPay(10000, 38))
