def solution(s):
    arr_a = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    for i in range(len(arr_a)):
        s =s.replace(arr_a[i],f"{i}")
    return int(s)