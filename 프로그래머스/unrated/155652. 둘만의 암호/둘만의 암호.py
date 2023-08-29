from collections import defaultdict
def solution(s, skip, index):
    answer = ''
    alp = sorted(list(set("abcdefghijklmnopqrstuvwxyz")-set(skip)))
    data = defaultdict(int)
    for i,v in enumerate(alp):
        data[v] = i
    return ''.join([alp[(data[i]+index)%len(alp)] for i in s])