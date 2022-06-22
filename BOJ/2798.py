# 블랙잭

import sys
n, m = map(int,sys.stdin.readline().split())

cards = list(map(int, sys.stdin.readline().split()))
sums = []

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sums.append(cards[i] + cards[j] + cards[k])

min_idx = -1
min_val = 99999999
for i,s in enumerate(sums):
    if s > m:
        continue

    if s==m:
        min_idx, min_val = i, m-s
        break

    if (m-s) < min_val:
        min_idx, min_val = i, m-s

print(sums[min_idx])
