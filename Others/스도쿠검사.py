import sys
sys.stdin = open('input.txt', 'rt')

# Solve 1
li = [list(map(int, input().split())) for _ in range(9)]

def check(sudoku):
    for i in range(9):
        check_row = [0] * 10
        check_col = [0] * 10
        for j in range(9):
            check_row[li[i][j]] = 1
            check_col[li[j][i]] = 1
        if sum(check_row) != 9 or sum(check_col) != 9:
            return False
            
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            check = [0] * 10
            
            for k in range(3):
                for s in range(3):
                    check[li[i+k][j+s]] = 1
        
            if sum(check) != 9:
                return False
    return True


if check(li):
    print('YES')
else:
    print('NO')

# Solve 2
# li = [list(map(int, input().split())) for _ in range(9)]

# answer = 'YES'

# for i in range(9):
#     check_row = [k for k in range(1,10)]
#     check_col = [k for k in range(1,10)]
#     for j in range(9):
#         # 행 검사
#         try:
#             check_row.remove(li[i][j])
#         except:
#             answer = 'NO'
#         # 열 검사
#         try:
#             check_col.remove(li[j][i])
#         except:
#             answer = 'NO'

# dx = [0, 0, 0, 1, 1, 1, 2, 2, 2]
# dy = [0, 1, 2, 0, 1, 2, 0, 1, 2]

# for i in range(0, 9, 3):
#     for j in range(0, 9, 3):
#         nums = [li[i+dx[k]][j+dy[k]] for k in range(9)]  # 9개 숫자
#         check = [k for k in range(1,10)]
#         for x in nums:
#             try:
#                 check.remove(x)
#             except:
#                 answer = 'NO'
# print(answer)
