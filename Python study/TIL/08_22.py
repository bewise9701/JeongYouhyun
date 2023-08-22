str_li = []
int_li = []
result = ''
num = 0
# upper를 설정하는 이유는 대문자만 입력하라는 조건이 설정되어있음.
inp = list(input().upper())
# 문자열과 수를 분리하여 저장함. => int_li, str_li 로 저장
for _ in inp:
    if _.isdigit():
        int_li.append(_)
    else:
        str_li.append(_) 

# int_li의 수를 모두 더함. => num
for _ in int_li:
    num += int(_)

# str_li를 정렬하여 결과값에 더해줌.
for _ in sorted(str_li):
    result += _

# 정렬된 문자열과 더해진 숫자를 합쳐줌.
result += str(num)
print(result)
    

