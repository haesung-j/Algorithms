# 1 2 3 4 10 9 8 7 13 12 11 5 6 14 15 16 17 18 19 20
import sys
sys.stdin = open('input.txt', 'r')
li = [i for i in range(1,21)]
a,b = 2, 5

for _ in range(10):
    a,b = map(int,input().split())
    li[a-1:b] = li[a-1:b][::-1]

for i in li:
    print(i, end=' ')
