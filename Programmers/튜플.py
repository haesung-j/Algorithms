import re
import ast
from collections import Counter
def solution(s):
    answer = []
    s = re.sub('{', '[', s)
    s = re.sub('}', ']', s)
    s = ast.literal_eval(s)
    tmp = []
    for i in s:
        for j in i:
            tmp.append(j)
            
    for k,v in Counter(tmp).most_common():
        answer.append(k)
    
    return answer