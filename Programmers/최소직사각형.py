def solution(sizes):
    l1 = []
    l2 = []
    for s in sizes:
        s.sort()
        l1.append(s[0])
        l2.append(s[1])
        
    return max(l1) * max(l2)
