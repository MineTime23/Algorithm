def solution(myString, pat):
    myString = myString.replace("A","1").replace("B","2").replace("2","A").replace("1","B")
    
    return int(pat in myString)