# 크로아티아 알파벳

S = input()
while True:
    if 'dz=' in S:
        S = S.replace('dz=', '!')
    else:
        break

li = ['c=', 'c-', 'd-', 'lj', 'nj', 's=','z=']
for l in li:
    while True:
        if l in S:
            S = S.replace(l,'!')
        else:
            break

print(len(S))