def transform_3(num, x):
    res = ''
    while True:  # 바로 앞뒤 반전
        if num < 3:
            res += str(num)
            break
        rest = num % 3
        res += str(rest)
        num = num // 3
    return res



def solution(n):
    num = transform_3(n, 3)
    num = int(num,3)
    return num
