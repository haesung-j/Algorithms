word = input()

res = ''
for c in word:
    if c.isalpha():
        continue
    else:
        res += c

res = int(res)

cnt = 0
for i in range(1, res+1):
    if res % i == 0:
        cnt += 1

print(res)
print(cnt)
