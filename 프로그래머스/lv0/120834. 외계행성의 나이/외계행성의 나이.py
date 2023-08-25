def solution(age):
    return ''.join([str(chr(int(i)+97)) for i in str(age)])