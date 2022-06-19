N = int(input())
scores = list(map(int,input().split()))

max_s = max(scores)
mean_s = sum(scores)/len(scores)

print(mean_s/max_s * 100)
