import re
def solution(my_string):
    my_string = re.sub(r'[aeiou]','',my_string)
    return my_string