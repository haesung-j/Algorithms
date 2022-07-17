from audioop import lin2alaw
import sys
sys.stdin = open('input.txt', 'rt')

n = int(input())
li = []
for _ in range(n):
    h,w = map(int, input().split())
    li.append((h,w))
    
li.sort(reverse=True)

max_w = 0
cnt = 0
for h,w in li:
    if w > max_w:
        max_w = w
        cnt += 1
        
print(cnt)
    
# li.sort(key=lambda x: (x[0]))
# cnt = 0
# for i in range(n):
#     crit = li[i][1]
#     for j in range(i+1, n):
#         if crit < li[j][1]:
#             break
#     else:
#         cnt += 1
        
# print(cnt)

