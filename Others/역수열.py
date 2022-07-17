import sys
sys.stdin = open('input.txt', 'rt')

n = int(input())
li = list(map(int, input().split()))


'''
[8]
[8, 7]
[8, 6, 7]
[8, 6, 5, 7]
[4, 8, 6, 5, 7]
[4, 8, 6, 5, 3, 7]
[4, 8, 6, 2, 5, 3, 7]
[4, 8, 6, 2, 5, 1, 3, 7]
'''
i = 0
num = n
original = []

while len(original) < n:
    original.insert(li[(n-1)-i], num)
    num -= 1
    i += 1
    
for x in original:
    print(x, end= ' ')
