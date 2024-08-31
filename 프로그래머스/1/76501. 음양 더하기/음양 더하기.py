def solution(absolutes, signs):
    
    return sum([absolutes[i] if a else -absolutes[i] for i,a in enumerate(signs)])


