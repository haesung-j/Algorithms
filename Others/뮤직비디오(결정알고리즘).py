from operator import lt
import sys
sys.stdin = open('input.txt', 'rt')

n,m = map(int, input().split())
li = list(map(int, input().split()))

'''
정답: 1 ~ sum(li)
'''

# 모든 영상을 녹화할 수 있는 DVD 개수를 계산하는 함수
def Count(x):
    cnt = 1
    xx = x
    for a in li:
        x -= a
        if x < 0:
            cnt += 1
            x = xx - a
    return cnt


lt = 1
rt = sum(li)

while lt <= rt:
    mid = (lt + rt) // 2
    # 요구되는 m개보다 작거나 같은 경우 정답에 저장
    if Count(mid) <= m:
        res = mid
        rt = mid - 1
        
    else:
        lt = mid + 1
        
print(res)