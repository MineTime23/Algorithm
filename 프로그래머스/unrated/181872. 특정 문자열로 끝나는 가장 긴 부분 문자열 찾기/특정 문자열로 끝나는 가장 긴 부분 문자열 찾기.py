def solution(myString, pat):
    copy_myString = myString[::]
    myString = myString[::-1]
    idx = myString.index(pat[::-1])
    print(idx)
    return (pat[::-1] + myString[idx+len(pat):])[::-1]