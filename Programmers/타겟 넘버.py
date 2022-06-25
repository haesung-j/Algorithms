# bfs
def solution(numbers, target):
    li = [numbers[0], -numbers[0]]
    
    for i in range(1, len(numbers)):
        nxt = numbers[i]
        nxt_li = []
        for num in li:
            nxt_li.append(num+nxt)
            nxt_li.append(num-nxt)
            
        li = nxt_li
    
    answer = sum(map(lambda x: x == target, li))
    
    return answer

## dfs
# cnt = 0
# def dfs(numbers, idx, target, s):
#     global cnt
#     if idx == len(numbers):
#         if s == target:
#             cnt += 1
#             return
#         else:
#             return
    
#     dfs(numbers, idx+1, target, s+numbers[idx])
#     dfs(numbers, idx+1, target, s-numbers[idx])


# def solution(numbers, target):
#     global cnt
#     dfs(numbers, 0, target, 0)
#     return cnt