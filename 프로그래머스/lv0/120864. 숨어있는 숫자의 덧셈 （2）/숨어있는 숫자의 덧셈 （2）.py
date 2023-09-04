import re
def solution(my_string):
    my_string = my_string.lower()
    my_string = re.sub("[a-z]"," ",my_string).split()
    return sum(map(int,my_string))