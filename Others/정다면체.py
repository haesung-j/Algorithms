n, m = map(int, input().split())

li = [0] * (n+m+1)    # 인덱스가 합에 바로 대응되도록 생성

for i in range(1, n+1):
    for j in range(1, m+1):
        li[i+j] += 1

for i,s in enumerate(li):
    if s == max(li):
        print(i, end=' ')
