def solution(n):
    n = bin(n)[2:]
    re_n = n[::-1]
    for i in range(len(re_n)):
        if i > 0 and (re_n[i-1] == "1" and re_n[i] == "0"):
            return int((''.join(sorted(re_n[:i-1],reverse=True)) + "01" + re_n[i+1:])[::-1],2)
    return int((''.join(sorted(re_n[:-1],reverse=True)) + "01")[::-1],2)