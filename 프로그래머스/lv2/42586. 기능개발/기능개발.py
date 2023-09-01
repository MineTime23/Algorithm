from collections import Counter

def solution(progresses, speeds):
    progresses = list(map(lambda x : 100 - x, progresses))
    progresses = [ progresses[i]//speeds[i] if progresses[i] % speeds[i] == 0 else progresses[i]//speeds[i] + 1 for i in range(len(progresses))]
    
    for i in range(len(progresses)):
        if i == 0: 
            continue
        else:
            if progresses[i] < progresses[i-1]:
                progresses[i] = progresses[i-1]
    return list(Counter(progresses).values())