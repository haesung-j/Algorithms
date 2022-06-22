# 마침표(.) 압축 함수
def comp(x):
    x += ' '   # 마지막 .을 처리하기 위함
    res = ''
    cnt = 0
    i = 0
    while i < len(x):  # 끝까지 탐색하면 종료
        if x[i] == '.':
            i += 1
            cnt += 1
            continue
            
        if x[i] != '.':
            if cnt == 0:
                res += x[i]
            else:
                res += '.' + x[i]
            
            i += 1
            cnt = 0  
    return res.rstrip()

# 마침표 압축을 다음과 같이 처리 가능
# txt = '...awdwa..dawgf.awdg...'
# while '..' in txt:
#     txt = txt.replace('..', '.')
#     print(txt)

def solution(new_id):
    answer = ''
    allow_char = ['-', '_', '.']
    
    # step 1
    new_id = new_id.lower()
    
    # step 2
    new_id_p = ''
    for c in new_id:
        if ('a' <= c <= 'z') or ('0' <= c <= '9') or (c in allow_char):
            new_id_p += c
            
    new_id = new_id_p
    
    # step 3
    new_id = comp(new_id)
    
    # step 4
    if len(new_id) > 0:
        if new_id[0] == '.':
            new_id = new_id[1:]
            
    if len(new_id) > 0:
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    # step 5      
    if len(new_id) == 0:
        new_id = 'a'
        
    # step 6   
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    # step 7
    if len(new_id) <= 2:
        last = new_id[-1]
        while len(new_id) < 3:
            new_id += last

    return new_id


inputs = ["...!@BaT#*..y.abcdefghijklm",
          "z-+.^.",
          "=.=",
          "123_.def",
          "abcdefghijklmn.p" ]

results = [	"bat.y.abcdefghi",
           "z--",
           "aaa",
           "123_.def",
           "abcdefghijklmn"]

answers = list(map(solution, inputs))
for a,r in zip(answers, results):
    print('출력: {}  정답: {}'.format(a,r))
