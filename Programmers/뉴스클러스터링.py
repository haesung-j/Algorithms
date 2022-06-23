import numpy as np

def solution(str1, str2):
    ## ==소문자로== ##
    str1 = str1.lower()
    str2 = str2.lower()
    
    ## ==두글자씩 끊고 특수문자 제거해 딕셔너리== ##
    s1 = dict()
    s2 = dict()

    i = 1
    while i < len(str1):
        if ('a'<= str1[i] <= 'z') and ('a'<= str1[i-1] <= 'z'):
            word = str1[i-1]+str1[i]
            s1[word] = s1.get(word,0) + 1
        i += 1


    i = 1
    while i < len(str2):
        if ('a'<= str2[i] <= 'z') and ('a'<= str2[i-1] <= 'z'):
            word = str2[i-1]+str2[i]
            s2[word] = s2.get(word,0) + 1
        i += 1
        
    ## ==합집합과 교집합 개수 구하기== ##
    cnt_union = 0
    cnt_intersect = 0
    # s1에 대한 값들을 세면서 s2에도 존재한다면 maximum값을 합집합 개수에 더해주기
    for k1,v1 in s1.items():
        v2 = s2.get(k1,0)
        cnt_union += max(v1,v2)
        # 만약 s2에도 존재한다면, 중복으로 세지 않기 위해 s2에서 해당 단어 지움
        # 만약 s2에도 존재한다면, 교집합이므로 더 작은 개수를 더함
        if v2 != 0:
            cnt_intersect += min(v1,v2)
            del s2[k1]
    # s2에 남은 값들에 대해 합집합 개수 더해주기
    for k2,v2 in s2.items():
        cnt_union += v2
    
    if cnt_union == 0:
        res = 65536
    else:
        res = cnt_intersect/cnt_union * 65536
    
    return int(np.trunc(res))