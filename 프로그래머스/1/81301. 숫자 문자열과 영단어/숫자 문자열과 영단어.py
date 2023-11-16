trans = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}

def solution(s):
    for a in trans.items():
        s = s.replace(a[0],str(a[1]))
    return int(s)