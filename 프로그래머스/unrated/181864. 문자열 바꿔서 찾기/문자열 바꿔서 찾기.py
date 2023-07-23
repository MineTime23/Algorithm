def solution(myString, pat):
    myString = myString.replace("A","1")
    myString = myString.replace("B","2")
    myString = myString.replace("2","A")
    myString = myString.replace("1","B")
    return int(pat in myString)