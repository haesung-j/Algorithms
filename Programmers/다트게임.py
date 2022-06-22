def solution(dart):
    # 라운드별 기록 추출
    i, j = 1, 0
    li = []
    while i < len(dart):
        if ('0' <= dart[i] <= '9'):
            if not ('0' <= dart[i-1] <= '9'):
                li.append(dart[j:i])
                j = i
        i += 1
    li.append(dart[j:])
    
    # 옵션 처리 부분
    need_minus = [False] * len(li)
    need_double = [False] * len(li)
    cal_li = []
    for i,l in enumerate(li):
        if l[-1] == '#':
            need_minus[i] = True
            l = l[:-1]
        if l[-1] == '*':
            need_double[i] = True
            l = l[:-1]
        
        cal_li.append(l)
    
    # 점수 계산
    scores = []
    for i,c in enumerate(cal_li):
        score = int(c[:-1])
        scores.append([score, c[-1]])
    
    scores2 = []
    for i, ss in enumerate(scores):       
        if ss[1] == 'S':
            s = ss[0]
        if ss[1] == 'D':
            s = ss[0]**2
        if ss[1] == 'T':
            s = ss[0]**3
        
        scores2.append(s)
    
    for i in range(3):
        if need_double[i]:
            if i == 0:
                scores2[i] *= 2
            else:
                scores2[i-1] *= 2
                scores2[i] *= 2
        
        if need_minus[i]:
            scores2[i] = -scores2[i]
    return sum(scores2)
