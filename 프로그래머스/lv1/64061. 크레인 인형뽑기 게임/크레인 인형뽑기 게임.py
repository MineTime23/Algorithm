result = []
answer = 0

def mv(board, n):
    global answer
    for i in range(len(board[0])):
        if board[n][i] != 0:
            if result and result[-1] != board[n][i]:
                result.append(board[n][i])
            elif result and result[-1] == board[n][i]:
                result.pop()
                answer += 2
            elif not result:
                result.append(board[n][i])
            board[n][i] = 0
            break

def solution(board, moves):
    board = list(map(list,zip(*board)))
    for i in moves:
        mv(board, i-1)
    return answer