import sys
sys.stdin = open('input.txt', 'rt')

n = int(input())
li = list(map(int, input().split()))
m = int(input())


for _ in range(m):
    li[li.index(max(li))] -= 1
    li[li.index(min(li))] += 1
    
print(max(li) - min(li))
