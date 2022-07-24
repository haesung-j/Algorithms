def make2(x, n):
    res = ''
    while x >= 2:
        res += str(x % 2)
        x = x // 2

    res += str(x)
    if len(res) < n:
        while len(res) < n:
            res += '0'
    res = res[::-1]
    return res

def combine(xs, ys):
    res = ''
    for i, (x,y) in enumerate(zip(xs,ys)):
        if x == '0' and y == '0':
            res += ' '
        else:
            res += '#'
    return res

def solution(n, arr1, arr2):
    answer = []
    
    for a,b in zip(arr1, arr2):

        xs = make2(a, n)
        ys = make2(b, n)
        res = combine(xs, ys)
        answer.append(res)
    
    
    return answer
