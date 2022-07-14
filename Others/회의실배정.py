import sys
sys.stdin = open('input.txt', 'rt')

n = int(input())

li = []

for _ in range(n):
    li.append(list(map(int, input().split())))
    
# 회의 시간이 끝나는 순서대로 정렬
li = sorted(li, key = lambda x: (x[1], x[0]))

end_time = 0
cnt = 0

for st, ed in li:
    if st >= end_time:
        cnt += 1
        end_time = ed
        
print(cnt)