import sys
sys.stdin = open('input.txt', 'rt')

from collections import deque
ness = list(input())
n = int(input())

for i in range(n):
    plans = list(input())
    plans = deque(plans)
    
    order = []
    for p in plans:
        if (p in ness) and p not in order:
                order.append(p)
                
    if order == ness:
        print(f'#{i+1} YES')
    else:
        print(f'#{i+1} NO')