# 소수(에라토스테네스 체)
# 2부터 시작해서 수를 하나씩 늘리며 해당 수의 배수를 지워나가는 방식
n = int(input())

sosu = [False]*2 + [True]*(n-1)

for i in range(2, n+1):
    if sosu[i]:
        for j in range(i*2, n+1, i):
            sosu[j] = False

s = [i for i in range(2,n+1) if sosu[i]==True]

print(len(s))
