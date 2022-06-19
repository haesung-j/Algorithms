# 셀프 넘버
numbers = set([i for i in range(1,10000)])
for i in range(1, 10000):
    num = str(i)
    sum_n = i
    for n in num:
        sum_n += int(n)

    numbers.discard(sum_n)

for n in numbers:
    print(n)