def digit_sum(x):
    s = 0
    while x > 0:
        s += x % 10
        x = x // 10
    return s

n = int(input())
li = list(map(int,input().split()))

max_x = -1
for x in li:
    if digit_sum(x) > max_x:
        max_x, res = digit_sum(x), x

print(res)
