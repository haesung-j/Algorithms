li = [list(map(int, input().split())) for _ in range(7)]

def isround(x):
    for i in range(len(x)//2):
        if x[i] != x[-i-1]:     
            return False
    return True

cnt = 0
for i in range(7):
    for j in range(3):
        # 행 검사
        if isround(li[i][j:j+5]):
            cnt += 1


# 열 검사

for i in range(7):
    for j in range(3):
        col = []
        for k in range(5):
            col.append(li[j+k][i])

        if isround(col):
            cnt+=1

print(cnt)
