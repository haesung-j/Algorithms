first = [1,2,3,4,5]
second = [2, 1, 2, 3, 2, 4, 2, 5]
third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

def solution(answers):
    # 정답 count
    f_cnt, s_cnt, t_cnt = 0, 0, 0
    for i,a in enumerate(answers):
        if first[i%len(first)] == a:
            f_cnt += 1
        if second[i%len(second)] == a:
            s_cnt += 1
        if third[i%len(third)] == a:
            t_cnt += 1
    cnt = [f_cnt, s_cnt, t_cnt]
    
    
    # 높은 점수 사람 반환
    # 동점일 경우 오름차순
    max_score = max(cnt)
    
    answer = []
    for i in range(3):
        if cnt[i] == max_score:
            answer.append(i+1)
    
    return answer
