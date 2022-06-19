# 그룹 단어 체커
count = 0
N = int(input())
for _ in range(N):
  S = input()
  uni = set(S)
  
  cnt = 0
  for u in uni:
      idx = []
      for i, s in enumerate(S):
          if u == s:
              idx.append(i)
      for k in range(1,len(idx)):
          if idx[k] != idx[k-1] + 1:
              cnt = 1
              
  if cnt == 0:
      count += 1
print(count)