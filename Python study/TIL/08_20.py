# 4번 문제
n = int(input())
coin = list(map(int, input().split()))

# 동전을 정렬함.
coin.sort()

# 여기까지는 풀었음... 밑에부분은 답안에 나와있는 설명...

target = 1
for i in coin:
    # 만들 수 없는 금액이 나오면 종료시키기
    if target < i:
        break
    # 그렇지 않다면 리스트의 금액 더하기
    target += i
# 만들 수 없는 금액의 최솟값을 출력하기.
print(target)

# 5번은 이해를 못하겠다... 누가 설명좀??
