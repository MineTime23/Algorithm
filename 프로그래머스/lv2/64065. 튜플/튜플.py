from collections import Counter
import re

def solution(s):
    answer = []
    s = re.sub("[{}]","",s)
    #print(s)
    s = s.split(",")
    s = list(map(int, s))
    answer = Counter(s)
    answer = list(answer.items())
    answer = sorted(answer,key=lambda x : -x[1])  
    return [a for a,b in answer]