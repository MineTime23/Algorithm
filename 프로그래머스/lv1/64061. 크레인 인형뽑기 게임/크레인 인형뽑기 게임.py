def solution(board, moves):
    answer = 0
    arrange = []
    basket = []
    
    for x in range(len(board)):
        new = []
        for y in range(len(board)-1,-1,-1):
            new.append(board[y][x])
        arrange.append(new)
    #print(arrange)
    
    for i in moves:
        cnt = 0
        for j in range(len(arrange[i-1])):
            if arrange[i-1][j] == 0:
                break
            else:
                cnt += 1
        if cnt == 0:
            continue
        else:
            if basket and basket[-1] == arrange[i-1][cnt-1]:
                answer += 2
                basket.pop()
            else:
                basket.append(arrange[i-1][cnt-1])
            arrange[i-1][cnt-1] = 0
            
    #print(basket)
    return answer