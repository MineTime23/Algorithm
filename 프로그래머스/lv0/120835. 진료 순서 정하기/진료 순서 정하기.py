def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True)
    data = { v : i for i,v in enumerate(sorted_emergency)}
    return list(map(lambda x : data[x]+1, emergency))