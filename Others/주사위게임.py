from collections import Counter

def prize(li):
    if li[0] == li[1] and li[1]==li[2]:
        return 10000 + li[0]*1000

    a = Counter(li)
    if li[0] != li[1] and li[0] != li[2] and li[1]!=li[2]:
        a = sorted(a.items(), key=lambda x: -x[0])
        return a[0][0]*100


    else:
        a = sorted(a.items(), key=lambda x:-x[1])
        return 1000 + a[0][0]*100

n = int(input())

li = []
for i in range(n):
    part = list(map(int,input().split()))
    li.append(prize(part))

print(max(li))
