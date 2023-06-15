#2023.06.15 GPT 예제
#1번 문제
def count_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in text:
        if char.lower() in vowels:
            count += 1
    return count

# 문제에서 주어진 문자열
text = "Hello, how are you?"

# 주어진 문자열에서 모음의 개수를 세는 함수 호출
vowel_count = count_vowels(text)

# 결과 출력
print("모음의 개수:", vowel_count)

"""처음 시도할 때 결과 값이 계속 1이 나왔던 이유
: return 함수가 for과 같은 수준에 있어야했는데, if 함수 안에 있어서 retrun 함수의 값을 제대로 받지 못했다."""


#2번 문제(혼자 해봄)
#백만이 넘으면 단위로 M이 붙게 하고, 10억이 넘으면 B가 붙게하기(소수점 1자리까지 표시됨.)
def change_numbers(number):
    if number > 1000000000:
        Bil = int(number/100000000)/10
        print(Bil, f"B ({number})$")
    elif  number > 1000000:
        Mil = int(number/100000)/10
        print(Mil, f"M ({number})$")
    else:
        print(number)

change_numbers(344400000)
# 344.4B로 나옴.
