def solution(a, b):
    days = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    weekday = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    return weekday[(sum(days[:a]) + b-1)%7]