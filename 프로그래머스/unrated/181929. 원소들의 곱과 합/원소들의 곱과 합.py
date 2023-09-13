def solution(num_list):
    answer = 0
    return int(eval("*".join(map(str,num_list)))< sum(num_list)**2 )