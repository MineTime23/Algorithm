def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        new_arr = []
        for j in range(len(arr2[0])):
            cnt = 0
            for k in range(len(arr2)):
                cnt += arr1[i][k] * arr2[k][j]
            new_arr.append(cnt)
        answer.append(new_arr)
    return answer