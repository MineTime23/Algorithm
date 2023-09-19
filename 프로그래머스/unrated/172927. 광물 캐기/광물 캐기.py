def solution(picks, minerals):
    answer = 0
    arr1 = []
    data = {2 : 25, 1 : 5, 0 : 1, -1 : 1, -2 : 1}
    data2 = {"diamond" : 0, "iron" : 1, "stone":2}
    minerals = list(map(lambda x : data2[x],minerals))

    for i in range(0,len(minerals),5):

        arr2 = minerals[i:i+5]
        arr1.append(arr2)
    #print(arr1)
    if sum(picks) < len(minerals)//5 if len(minerals)%5 == 0 else len(minerals)//5 +1:
        arr1 = arr1[:sum(picks)]
    #print(arr1)
    arr1 = sorted(arr1, key = lambda x : (-x.count(0), -x.count(1), -x.count(2)))
    #print(arr1)
    idx = 0
    for i in range(min(sum(picks),len(arr1))):
        while picks[idx] == 0:
            idx += 1
        new = sum(list(map(lambda x: data[idx-x],arr1[i])))
        answer += new
        picks[idx] -= 1
    
    return answer