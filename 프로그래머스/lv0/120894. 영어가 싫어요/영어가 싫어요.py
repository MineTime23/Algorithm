def solution(numbers):
    answer = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i,v in enumerate(answer):
        numbers = numbers.replace(v,str(i))
    return int(numbers)