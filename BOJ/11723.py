# 집합
import sys
n  = int(sys.stdin.readline())
# inp = sys.stdin.readline().rstrip()

li = []
for _ in range(n):
    inp = sys.stdin.readline().rstrip().split()
    if len(inp) == 1:
        op = inp[0]
    else:
        op, num = inp[0], int(inp[1])

    if op == 'add' and num not in li:
        li.append(num)
    if op == 'remove' and num in li:
        li.remove(num)
    if op =='toggle':
        if num not in li:
            li.append(num)
        else:
            li.remove(num)

    if op == 'all':
        li.clear()
        li = [i for i in range(1,21)]

    if op =='empty':
        li.clear()

    if op == 'check':
        if num in li:
            print(1)
        else:
            print(0)
