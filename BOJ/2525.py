# 오븐 시계

# A, B: 요리 시작 시간
A,B = map(int,input().split())
# C: 요리 소요 시간
C = int(input())

cook_H = C // 60
cook_M = C % 60

cook_H = A + cook_H
add_H = (B + cook_M) // 60

total_H = cook_H + add_H
total_M = (B + cook_M )% 60

if total_H >= 24:
    print(total_H-24, total_M)
else:
    print(total_H, total_M)