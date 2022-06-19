S = input().upper()

li = [0 for _ in range(26)]
# 등장 개수 세기
for s in S:
    li[ord(s)-65] += 1

# 최대값이 하나가 아니라면 ? 출력
if len([x for x in li if x == max(li)]) != 1:
    print('?')
# 최대값이 하나라면 해당 인덱스 알파벳 출력(using chr)
else:
    print(chr(li.index(max(li))+65))
