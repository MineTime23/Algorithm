import heapq
def solution(k, score):
    answer = []
    heap = []
    for i in score:
        if len(heap) < k:
            heapq.heappush(heap,i)
        else:
            if heap[0] < i:
                heapq.heappop(heap)
                heapq.heappush(heap,i)
        answer.append(heap[0])
    return answer