from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    data = defaultdict(list)
    data2 = defaultdict(int)
    for i in records:
        arr = i.split()
        clock = arr[0].split(":")
        clock = int(clock[0]) * 60 + int(clock[1])
        if arr[-1] == "IN":
            data[arr[1]].append(-clock)
        else:
            data[arr[1]].append(+clock)
    for i in data:
        if len(data[i])%2 == 1:
            data[i].append(+1439)
        data2[i] = sum(data[i])
        if data2[i] > fees[0]:
            print(data2[i],fees[0],fees[2],fees[3])
            data2[i] = int(fees[1] + math.ceil((data2[i]-fees[0])/fees[2])*fees[3])
        else:
            data2[i] = int(fees[1]) 
    sorted_items = sorted(data2.items(), key=lambda x: x[0])  
    result = [x[1] for x in sorted_items]
    return result