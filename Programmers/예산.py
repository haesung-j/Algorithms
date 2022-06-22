def solution(d, budget):
    d.sort()
    cnt = 0
    s = 0
    for i in d:
        s += i
        if s > budget:
            break
        cnt += 1
    
    return cnt
