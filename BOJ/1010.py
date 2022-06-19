# 다리 놓기
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    res = factorial(m)/(factorial(m-n)*factorial(n))
    print(int(res))