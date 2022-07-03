def reverse(x):
    return x[::-1]

def is_prime(x):
    cnt = 0
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

n = int(input())
c_li = list(input().split())

for c in c_li:
    c = int(reverse(c))
    if is_prime(c):
        print(c, end=' ')
