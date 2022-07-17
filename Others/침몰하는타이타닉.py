import sys
sys.stdin = open('input.txt', 'rt')


'''
보트는 1명 또는 2명만 탑승 가능
보트 한 개에 탈 수 있는 무게 M kg 이하로 제한
승객 모두가 탈출하기 위한 구명 보트의 최소 개수
'''

n, m = map(int,input().split())
people = list(map(int, input().split()))


from collections import deque
people.sort(reverse=True)  # 가장 무거운 사람이 앞에 위치
people = deque(people)

cnt = 0
while people:   # 모든 사람이 탈 때까지
    if len(people) == 1:
        cnt += 1
        people.pop()
    
    
    elif people[0] + people[-1] > m:
        cnt += 1
        people.popleft()
        
    else:
        cnt += 1
        people.pop()
        people.popleft()
        
print(cnt)