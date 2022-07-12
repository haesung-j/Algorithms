import sys
sys.stdin = open('input.txt', 'rt')


n, c = map(int, input().split())

li = [int(input()) for _ in range(n)]

li.sort()


lt = 1
rt= li[-1]

def Count(x):
    cnt = 1
    pos = li[0]
    for i in range(1, n):
        if (li[i] - pos) >= x:
            cnt += 1
            pos = li[i]
    return cnt
        

while lt <= rt:
    mid = (lt+rt) // 2

    if Count(mid) >= c:
        res = mid
        lt = mid + 1
        
    else:
        rt = mid - 1

print(res)

# 1 2 4 8 9
