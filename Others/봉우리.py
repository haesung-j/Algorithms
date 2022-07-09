# import sys
# sys.stdin = open('input.txt', 'rt')

n = int(input())

maps = [[0]*(n+1)]


for _ in range(n):
    maps.append([0] + list(map(int, input().split())) + [0])

maps.append([0]*(n+1))
cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        pos = maps[i][j]
        
        if pos > maps[i-1][j] and pos > maps[i+1][j] and pos > maps[i][j+1] and pos > maps[i][j-1]:
            cnt += 1
print(cnt)