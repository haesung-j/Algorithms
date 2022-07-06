n = int(input())
li_1 = list(map(int,input().split()))

m = int(input())
li_2 = list(map(int,input().split()))

new_li = []

i = 0
j = 0
while len(new_li) < n+m:
    if li_1[i] < li_2[j]:
        new_li.append(li_1[i])
        i += 1
    else:
        new_li.append(li_2[j])
        j += 1

    if i == n:
        new_li += li_2[j:]
    if j == m:
        new_li += li_1[i:]

for x in new_li:
    print(x, end=' ')
