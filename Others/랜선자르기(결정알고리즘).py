import sys
sys.stdin = open('input.txt', 'rt')

k, n = map(int, input().split())

li = [int(input()) for _ in range(k)]

cnt = 0

start = 1
end = max(li)+1

while start <= end:
    mid = (start+end) // 2
    cnt = 0 
    for x in li:
        cnt += x // mid
    if cnt >= n:
        res = mid
        start = mid + 1
    else:
        end = mid -1
        
print(res)


