def move(order):
    row = order[0] - 1
    direction = order[1]
    steps = order[2]
    for step in range(steps):
        if direction == 0:
            element = li[row].pop(0)
            li[row].append(element)
        elif direction == 1:
            element = li[row].pop()
            li[row] = [element] + li[row]

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for _ in range(m):
    order = list(map(int, input().split()))
    move(order)

start = -1
end = n+1

s = 0
for i in range(n):
    if i <= n // 2:
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1
    for j in range(start,end):
        s += li[i][j]

print(s)
