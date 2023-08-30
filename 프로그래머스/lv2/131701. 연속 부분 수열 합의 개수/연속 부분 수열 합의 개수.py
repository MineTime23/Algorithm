def solution(elements):
    elements = elements * 2
    sumt = set()
    for i in range(len(elements)//2):
        for j in range(len(elements)//2):
            sumt.add(sum(elements[i:i+j+1]))
    return len(sumt)