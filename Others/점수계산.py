n = int(input())
answer = list(map(int, input().split()))

for i in range(1, len(answer)):
    if answer[i] == 0:
        continue
    else:
        answer[i] = answer[i] + answer[i-1]

print(sum(answer))
