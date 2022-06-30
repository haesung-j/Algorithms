def digit_sum(x):
    s = 0
    while True:
        num = x % 10
        s += num

        x = x // 10
        if x == 0:
            break
    return s

n = int(input())

li = list(map(int,input().split()))

max_x = -1
for x in li:
    if digit_sum(x) > max_x:
        max_x = digit_sum(x)
        res = x

print(res)
