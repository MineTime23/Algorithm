import re
def solution(my_string):
    my_string = re.sub(r'[a-zA-Z]','',my_string)
    return sum(map(int,list(my_string)))