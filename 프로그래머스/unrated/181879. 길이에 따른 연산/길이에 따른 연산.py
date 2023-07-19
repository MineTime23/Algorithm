def solution(num_list):
    answer = 0
    return eval("*".join(map(str,num_list)))if len(num_list) <= 10 else sum(num_list)