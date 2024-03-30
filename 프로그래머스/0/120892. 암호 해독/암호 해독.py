def solution(cipher, code):
    return ''.join([a for i,a in enumerate(cipher) if (i+1)%code == 0])