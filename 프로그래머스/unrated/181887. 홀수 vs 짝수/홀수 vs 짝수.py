def solution(num_list):
    return max(sum([v for i,v in enumerate(num_list) if i%2 == 0]),sum([v for i,v in enumerate(num_list) if i%2 == 1]))