from collections import deque
def solution(priorities, location):
    cnt = 0
    documents = [chr(65+i) for i in range(len(priorities))]  # 문서마다 uniqueness 부여
    target = documents[location]  # 순서를 찾고자 하는 문서
    
    # queue를 사용하기 위해 자료구조 변환
    docu = deque(documents)  
    prior = deque(priorities)
    
    # prior가 빌 때까지(모든 문서가 출력될 때까지)
    while prior:
        node = prior.popleft()   # 맨 앞 문서의 중요도를 가져옴
        alpha = docu.popleft() # 맨 앞 문서를 가져옴
        for p in list(prior):      # 나머지 문서들과 중요도 비교
            if node >= p:             # 현재 문서가 나머지보다 중요도가 높다면 통과
                continue
            else:                         # 현재 문서보다 중요도가 높은 문서가 있다면 현재 문서를 맨 뒤로
                prior.append(node)
                docu.append(alpha)
                break
        else:  # 모든 문서보다 현재 문서의 중요도가 높다면
            cnt += 1  # 출력 순서 부여
            if alpha == target: # 현재 문서가 원하는 문서라면 출력 순서 반환
                return cnt
