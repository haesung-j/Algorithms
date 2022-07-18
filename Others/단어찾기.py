import sys
sys.stdin = open('input.txt', 'rt')

n = int(input())

words = [input() for _ in range(n)]

for _ in range(n-1):
    words.remove(input())
    
print(words[0])

# words = dict()
# for _ in range(n):
#     w = input()
#     words[w] = words.get(w, 0) + 1
    
# for _ in range(n-1):
#     w = input()
#     words[w] -= 1
    
# for k,v in words.items():
#     if v == 1:
#         print(k)