def solution(numbers):
    # 0부터 9까지 숫자 중 numbers에 존재하지 않는 원소만 추출해 더하기
    return sum([x for x in list(range(10)) if x not in numbers])
