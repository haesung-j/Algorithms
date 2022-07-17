from os import name
import sys
sys.stdin = open('input.txt', 'rt')

num, m = input().split()
m = int(m)


num = list(num)

stack = []

for x in num:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
        
    stack.append(x)
    
if m > 0:
    stack = stack[:-m]

res = ''.join(map(str, stack))
print(int(res))