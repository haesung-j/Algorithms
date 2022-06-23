# 윤년: 2월 29일까지 존재
days = ['FRI', 'SAT','SUN','MON','TUE','WED','THU']
odds = [1,3,5,7,8,10,12]
evens = [4,6,9,11]

def find_dday(a,b):
    dday = 0
    if a == 1:
        return b-1
    
    month = [i for i in range(1,a)]
    
    for m in month:
        if m in odds:
            dday += 31
        elif m in evens:
            dday += 30
        else:
            dday += 29
    return dday + b - 1
    
def solution(a, b):
    d_day = find_dday(a,b)
    answer = days[d_day % 7]
    
    return answer
