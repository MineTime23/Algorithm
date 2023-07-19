def solution(a, b):
    day = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    month = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    da = b
    for i in range(a):
        da += month[i]
    return day[(da-1)%7]