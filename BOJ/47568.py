# 덩치
# 데이터 입력받기
n = int(input())
li = [tuple(map(int, input().split())) for _ in range(n)]

# 순차적으로 돌면서 자기보다 덩치가 큰 사람의 수를 셈 => 덩치가 큰 사람 수가 곧 순위
for w,h in li:
    rank = 1
    for x,y in li:
        if w < x and h < y:  # 자기 자신은 자동으로 filtering 됨
            rank += 1
    print(rank, end=' ')  
