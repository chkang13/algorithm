def solution(board, moves):
    stack = [] # 인형을 옮길 바구니
    answer = 0 # 터진 인형 수 저장
    
    for locate in moves:
        for i in range(len(board)):
            if board[i][locate-1] == 0:
                continue
            else:
                stack.append(board[i][locate-1])
                board[i][locate-1] = 0
        
                if len(stack) > 1:
                    if stack[-1] == stack[-2]:
                        stack.pop()
                        stack.pop()
                        answer += 2
                break
    
    return answer