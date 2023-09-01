def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        if i == 0:
            continue
        elif phone_book[i].startswith(phone_book[i-1]):
            return False
    return True