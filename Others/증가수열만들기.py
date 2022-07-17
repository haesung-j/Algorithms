import sys
sys.stdin = open('input.txt', 'rt')

'''
좌,우에서 수를 가져와 크기가 증가하는 수열 만들기
마지막에 남은 값은 왼쪽으로 생각
'''
from collections import deque

n = int(input())
nums = list(map(int, input().split()))

q = deque(nums)

cnt = 1

if q[0] < q[-1]:
    cur = q.popleft()
    res = 'L'
else:
    cur = q.pop()
    res = 'R'
    


while q:
    if q[0] < cur and q[-1] < cur:
        break

    if len(q) == 1:
        cnt += 1
        res += 'L'
        break

    if q[0] > q[-1]:
        if q[-1] > cur:
            cnt += 1
            cur = q.pop()
            res += 'R'
        else:
            cnt += 1
            cur = q.popleft()
            res += 'L'

    elif q[0] < q[-1]:
        if q[0] > cur:
            cnt += 1
            cur = q.popleft()
            res += 'L'
        else:
            cnt +=1
            cur = q.pop()
            res += 'R'

print(cnt)
print(res)