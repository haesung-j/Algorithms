n = int(input())

for i in range(1, n+1):
    c = input().lower()
    ans = 'YES' if c == c[::-1] else 'NO'

    print('#{} {}'.format(i, ans))
