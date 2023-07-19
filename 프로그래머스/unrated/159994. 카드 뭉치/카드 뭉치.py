def solution(cards1, cards2, goal):
    cnt = 0
    while cnt != (len(goal)):
        if cards1 and goal[cnt] == cards1[0]:
            cards1 = cards1[1:]
        elif cards2 and goal[cnt] == cards2[0]:
            cards2 = cards2[1:]
        else:
            return "No"
        cnt += 1    
    return "Yes"

solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"])