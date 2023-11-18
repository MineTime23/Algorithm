def solution(myString):
    myString = myString.split("x")
    return [i for i in sorted(myString) if i != ""]