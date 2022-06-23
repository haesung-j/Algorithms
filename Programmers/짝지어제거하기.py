## 시간 초과 해결 -> 입력이 100만이상이기 때문 -> stack 사용
def solution(s):
    answer = 0
    stack = ['A']

    i = 0
    while i < len(s):
        if stack[-1] != s[i]:
            stack.append(s[i])
        else:
            stack.pop()
        i += 1
        
    stack = stack[1:]
    if len(stack) == 0:
        return 1
    else:
        return 0


## 시간 초과
# def find_pair(x):  # 반복되는 문자가 있는지 검사하고, 반복되는 문자 반환
#     for i in range(len(x)-1):
#         if x[i] == x[i+1]:
#             return True, x[i]
#     return False, None

# def solution(s):
#     answer = -1
    
#     # 짝지어 제거하기 시작
#     while True:
#         A, u = find_pair(s) # 반복되는 문자가 있는지 검사
#         if not A: # 이어진 문자가 없다면 반복문 탈출
#             break
#         else:
#             s = s.replace(u+u, '')

#     if len(s)==0:
#         return 1
#     else:
#         return 0
