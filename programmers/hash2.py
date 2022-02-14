def solution(phone_book):
    phone_book.sort()
    for phone_number, tartget_phone_number in zip(phone_book, phone_book[1:]):
        if len(phone_number)<=1 or len(tartget_phone_number) <=1:
            pass
        elif phone_number.startswith(tartget_phone_number) or tartget_phone_number.startswith(phone_number):return False
    return True

print(solution(["12","123","1235","567","88"]))