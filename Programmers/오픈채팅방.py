def solution(record):
    answer = []
    d = {}

    for rec in record:
        if len(rec.split()) > 2:
            d[rec.split()[1]] = rec.split()[2]
            
    for rec in record:
        status = rec.split()[0]
        uid = rec.split()[1]
        
        if status == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(d[uid]))
        elif status == 'Leave':
            answer.append('{}님이 나갔습니다.'.format(d[uid]))    
    
    return answer