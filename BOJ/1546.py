N, M, K = map(int, input().split())
array = input().split()

for i in range(len(array)):
    array[i] = int(array[i])
  
# N은 배열 크기, M: 더해지는 횟수, K: 연속 최대등장횟수

array.sort(reverse=True)
sum = 0
k = 0

for _ in range(M):
  k += 1
  if k == K:
    sum += array[1]
    k = 0
  else:
    sum += array[0]
    
  
print(sum)
print(6*3 + 5 + 6*3 + 5)
