def solution(myString):
    return list(filter(lambda x : x != "",sorted(myString.split("x"))))