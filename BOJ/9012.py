# 괄호
## 풀이 1
n = int(input())
for _ in range(n):
    text = input()
    
    while '()' in text:
        text = text.replace('()','')
    if len(text) == 0:
        print('YES')
    else:
        print('NO')


## 풀이 2
# n = int(input())
# for _ in range(n):
#     text = input()
#     cnt = 0
    
#     for t in text:
#         if t == '(':       # 괄호가 열린 경우
#             cnt += 1
#         else:              # 닫힌 괄호인 경우
#             cnt -= 1
#             if cnt < 0:    # 열린 괄호보다 닫힌 괄호가 먼저 나온 경우
#                 print('NO')
#                 break
    
#     if cnt == 0:    # 열린 괄호 개수 = 닫힌 괄호 개수
#         print('YES')
#     elif cnt > 0:
#         print('NO')

## 풀이 3
# def rm_vps(text):
#     res = ''
#     i = 0
#     while i < len(text):
#         if i == len(text)-1:
#             res += text[i]
#             break
            
#         if (text[i]+text[i+1]) == '()':
#             i += 2
#         else:  
#             res += text[i]
#             i += 1
#     return res

    
# n = int(input())
# for _ in range(n):
#     text = input()
    
#     while '()' in text:
#         text = rm_vps(text)

#     if len(text) == 0:
#         print('YES')
#     else:
#         print('NO')