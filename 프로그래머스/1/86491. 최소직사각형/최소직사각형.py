def solution(sizes):
    result = [0,0]
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        result[0] = max(result[0], sizes[i][0])
        result[1] = max(result[1], sizes[i][1])
    return result[0] * result[1]