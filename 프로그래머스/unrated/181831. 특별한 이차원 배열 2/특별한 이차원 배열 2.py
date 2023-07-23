def solution(arr):
    answer = 0
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            if arr[y][x] != arr[x][y]:
                return 0
            if y == len(arr)//2 and x == len(arr[0])//2:
                return 1