import sys
sys.stdin = open('input.txt', 'rt')

n, k = map(int, input().split())
patients = list(map(int, input().split()))
nums = [i for i in range(len(patients))]

cnt = 0

while True:
  
    p = patients.pop(0)
    n = nums.pop(0)
    
    if p < max(patients):
        patients.append(p)
        nums.append(n)

    else:
        cnt += 1
        if n == k:
            break
    
print(cnt)
    