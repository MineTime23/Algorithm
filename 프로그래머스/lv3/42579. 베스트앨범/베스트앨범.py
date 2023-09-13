from collections import Counter, defaultdict

def solution(genres, plays):
    answer = []
    data = defaultdict(list)
    data2 = defaultdict(int)
    
    for i in range(len(genres)):
        data[genres[i]].append((-plays[i],i))
        data2[genres[i]] += plays[i]
        
    arr = data2.items()
    arr = sorted(arr, key = lambda x : -x[1])
    
    for a,b in arr:
        arr2 = sorted(data[a],key = lambda x : (x[0], x[1]))
        if len(arr2) >= 2:
            answer.append(arr2[0][1])
            answer.append(arr2[1][1])
        else:
            answer.append(arr2[0][1])
    return answer