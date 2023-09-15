import re
def solution(myString):
    myString = re.sub("[a-k]","l",myString)
    return myString