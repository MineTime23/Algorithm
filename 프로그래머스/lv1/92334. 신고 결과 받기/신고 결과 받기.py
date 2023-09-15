from collections import defaultdict

def solution(id_list, report, k):
    
    # 중복 신고 체크용
    repeattest = defaultdict(int)
    # 신고 받은 횟수 체크용
    cnt = defaultdict(int)
    # 메일 받을 수 있는지 체크용
    res = defaultdict(int)
    
    for i in report:
        if repeattest[i] == 0:
            repeattest[i] += 1
            arr = i.split()
            cnt[arr[1]] += 1
            
    repeattest = defaultdict(int) 
    
    for i in report:
        if repeattest[i] == 0:
            repeattest[i] += 1
            str1 = i.split()
            if cnt[str1[1]] >= k:
                res[str1[0]] += 1
    
    return [res[i] for i in id_list]