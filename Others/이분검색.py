import sys
sys.stdin = open('input.txt', 'rt')

n, m = map(int, input().split())
li = list(map(int,input().split()))
li.sort()

start = 0
end = n-1

while start <= end:
    mid = (start + end) // 2
    
    if li[mid] == m:
        print(mid + 1)
        break
    
    elif li[mid] > m:
        end = mid - 1
    
    else:
        start = mid + 1
        
