def solution(myString, pat):
    myString = myString.replace("A","C").replace("B","A").replace("C","B")
    #print(myString)
    return int(pat in myString)