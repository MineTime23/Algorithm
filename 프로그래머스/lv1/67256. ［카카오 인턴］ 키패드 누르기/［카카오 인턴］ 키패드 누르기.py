def solution(numbers, hand):
    answer = ''
    data = {1 : (0,0), 2 : (0,1), 3 : (0,2), 4 : (1,0), 5 : (1,1), 6 : (1,2), 7 : (2,0), 8 : (2,1), 9 : (2,2), "*": (3,0), 0 : (3,1), "#" : (3,2)}
    left_hand = (3,0)
    right_hand = (3,2)
    for i in numbers:
        if i in [1, 4, 7]:
            answer += "L"
            left_hand = data[i]
        elif i in [3, 6, 9]:
            answer += "R"
            right_hand = data[i]
        else:
            a,b = data[i]
            if abs(left_hand[0] - a) + abs(left_hand[1] - b) > abs(right_hand[0] - a) + abs(right_hand[1] - b):
                answer += "R"
                right_hand = data[i]
            elif abs(left_hand[0] - a) + abs(left_hand[1] - b) < abs(right_hand[0] - a) + abs(right_hand[1] - b):
                answer += "L"
                left_hand = data[i]
            else:
                if hand == "left":
                    answer += "L"
                    left_hand = data[i] 
                else:
                    answer += "R"
                    right_hand = data[i]                    
    return answer