def solution(numbers):
    sorted_numbers = sorted(map(str, numbers), key=lambda x: x * 10, reverse=True)
    if list(set(numbers)) == [0]:
        return "0"
    # 정렬된 숫자들을 문자열로 이어붙여 가장 큰 수 생성
    largest = ''.join(sorted_numbers)
    #print(sorted_numbers)
    
    return largest