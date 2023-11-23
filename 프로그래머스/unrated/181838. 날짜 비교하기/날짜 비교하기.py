def solution(date1, date2):
    data1 = int(''.join(list(map(str,date1))))
    data2 = int(''.join(list(map(str,date2))))
    return int(data1 < data2)