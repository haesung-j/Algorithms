n = int(input())
li = []
for _ in range(n):
    li.append(list(map(int, input().split())))

# Solve 1
sums = []
s = 0
for i in range(n):
    for j in range(n):
        s += li[i][j]
    sums.append(s)
    s = 0

s = 0
for j in range(n):
    for i in range(n):
        s += li[i][j]
    sums.append(s)
    s = 0

s = 0
for i in range(n):
    s += li[i][i]
sums.append(s)

print(max(sums))

## Solve 2
# sums = []
# max_sum = -1
# for i in range(n):
#     row_sum = 0
#     col_sum = 0
#     for j in range(n):
#         row_sum += li[i][j]
#         col_sum += li[j][i]
#     if row_sum > max_sum:
#         max_sum = row_sum
        
#     if col_sum > max_sum:
#         max_sum = col_sum
    
# sum_diag1 = 0
# sum_diag2 = 0
# for i in range(n):
#     sum_diag1 += li[i][i]
#     sum_diag2 += li[i][n-1 - i]
    
# if sum_diag1 > max_sum:
#     max_sum = sum_diag1
    
# if sum_diag2 > max_sum:
#     max_sum = sum_diag2
    
# print(max_sum)  
