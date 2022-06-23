def find(x):  # 약수의 개수를 찾는 함수
    cnt = 0
    for i in range(1, x+1):
        if x % i == 0:
            cnt += 1
    return cnt
    
def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        cnt = find(num)  
        if cnt % 2 == 0:    # 약수의 개수가 짝수개라면 더함
            answer += num
        else:              # 약수의 개수가 홀수개라면 뺌
            answer -= num
            
    return answer
