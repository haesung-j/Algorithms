import sys
sys.stdin = open('input.txt', 'rt')


pipe = input()

stack = []
cnt = 0
for i in range(len(pipe)):

    if pipe[i] == '(':
        stack.append(pipe[i])
        
    else: 
        if pipe[i-1] == '(':   # 레이저
            stack.pop()
            cnt += stack.count('(')
        else:  # 막대 끝
            stack.pop()
            cnt += 1
            
print(cnt)
        