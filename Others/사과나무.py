n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]


sums = 0
s = e = n // 2

for i in range(n):

	for k in range(s, e+1):
	sums += li[i][k]

	if i < n // 2:
		s -= 1
		e += 1

	else:
		s += 1
		e -= 1
		
		
# s = 0
# for i in range(n):
# 	if i <= n // 2:
# 		s += sum(li[i][(n-1)//2 - i : (n-1)//2+1 + i])
# 	else:
# 		s += sum(li[i][(n-1)//2 - (n-1-i) : (n-1)//2+1 + (n-1-i)])
# print(s)
