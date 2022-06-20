# 동전 0
import sys

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]

cnt = 0
for c in sorted(coins, reverse=True):
    if c > k:
        continue
    
    rest = k % c
    cnt += k // c
    
    k = rest
print(cnt)
