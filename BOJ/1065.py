# 한수
N = int(input())

if N < 100:
  cnt = N

else:
  cnt = 99
  for num in range(100, N+1):
      n = str(num)
      f, s, t = int(n[0]), int(n[1]), int(n[2])
      if (s - f) == (t - s):
          cnt += 1

print(cnt)