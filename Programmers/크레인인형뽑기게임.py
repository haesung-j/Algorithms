def solution(board, moves):
    n = len(board)
    cnt = 0
    queue = []
    for m in moves:
        
        for i in range(n):            
            if board[i][m-1] != 0:   # 인형이 존재하면 처리
                if len(queue) == 0 or queue[-1] != board[i][m-1]:  # 연속으로 같지 않으면 추가해줌
                    queue.append(board[i][m-1])
                
                else: # 연속으로 같으면 이전 값을 제거하고 cnt변수에 2개를 더해줌
                    queue.pop()
                    cnt += 2
                    
                board[i][m-1] = 0  # 인형을 뺀 효과 처리
                break
                
    return cnt
