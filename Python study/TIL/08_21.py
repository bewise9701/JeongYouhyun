# 이코테 2-7
point = list(str(input()))
a_re = 0
b_re = 0

a1 = (-len(point)//2)
a = point[:a1]
b = point[a1:]
for _ in a:
    i = int(_)
    a_re += i
for _ in b:
    i = int(_)
    b_re += i

if a_re == b_re:
    print("LUCKY")
else:
    print("READY")
    
