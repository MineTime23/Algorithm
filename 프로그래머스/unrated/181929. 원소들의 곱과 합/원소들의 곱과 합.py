def solution(num_list):
    a = sum(num_list)
    num_list = map(str, num_list)
    arr = int(eval("*".join(num_list)))
    return 1 if arr < a**2 else 0