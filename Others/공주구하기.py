from collections import deque

n, k = map(int, input().split())

prince = [i for i in range(1, n+1)]
prince = deque(prince)

while prince:
    
    for _ in range(k-1):
        prince.append(prince.popleft())
        
    prince.popleft()
    
    if len(prince) == 1:
        p = prince.pop()
        
print(p)
