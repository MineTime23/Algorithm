import heapq
def solution(k, score):
    answer = []
    honor = []
    heapq.heapify(honor)
    for i in score:
        if len(honor) <= k-1:
            heapq.heappush(honor,i)  
        else:
            heapq.heappush(honor,i)
            heapq.heappop(honor)
        answer.append(honor[0])    
    
    return answer