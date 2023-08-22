def solution(cards1, cards2, goal):
    a = 0
    b = 0
    for i in goal:
        if a<= len(cards1)-1 and i == cards1[a]:
            a += 1
        elif b<= len(cards2)-1 and i == cards2[b]:
            b += 1
        else:
            return "No"
    return "Yes"