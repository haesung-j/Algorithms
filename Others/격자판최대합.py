n = int(input())

li = []

for _ in range(n):
    li.append(list(map(int, input().split())))

sums = []
s = 0
for i in range(n):
    for j in range(n):
        s += li[i][j]
    sums.append(s)
    s = 0

s = 0
for j in range(n):
    for i in range(n):
        s += li[i][j]
    sums.append(s)
    s = 0

s = 0
for i in range(n):
    s += li[i][i]
sums.append(s)

print(max(sums))

