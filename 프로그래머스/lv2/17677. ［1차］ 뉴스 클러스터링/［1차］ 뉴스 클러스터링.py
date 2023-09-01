from collections import Counter
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1 = [str1[i:i+2]  for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    str2 = [str2[i:i+2]  for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    if len(Counter(str1)) == 0 and len(Counter(str2)) == 0:
        return 65536
    a = Counter(str1) & Counter(str2)
    b = Counter(str1) | Counter(str2)
    result = int(sum(list(a.values())) / sum(list(b.values())) * 65536)
    return result