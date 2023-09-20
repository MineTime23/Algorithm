def solution(triangle):
    for y in range(1,len(triangle)):
        for x in range(len(triangle[y])):
            if x == 0:
                triangle[y][x] += triangle[y-1][x]
            elif x == len(triangle[y])-1:
                triangle[y][x] += triangle[y-1][x-1]
            else:
                triangle[y][x] += max(triangle[y-1][x],triangle[y-1][x-1])
    #print(triangle)
    return max(triangle[-1])