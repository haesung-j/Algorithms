def solution(participant, completion):
    answer = ''
    
    p_dict = {}
    for p in participant:
        p_dict[p] = p_dict.get(p, 0) + 1
    
    for c in completion:
        p_dict[c] -= 1
    
    for k,v in p_dict.items():
        if v == 1:
            answer += k

    return answer
