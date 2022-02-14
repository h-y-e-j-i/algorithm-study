def solution(numbers):
    answer = ''
    numbers.sort()
    numbers_dict = dict()
    for num in numbers:
        if str(num)[0] not in numbers_dict.keys():
            numbers_dict[str(num)[0]] = list()

        if str(num) == 1 : find_prefix = str(num*11)
        else : find_prefix = str(num)[0:2]

        start_index = 0
        for index, value in zip(range(len(numbers_dict[str(num)[0]])), numbers_dict[str(num)[0]]):
            if str(value).startswith(find_prefix):
                start_index = index
                break

        find_index = -1
        for index, value in zip(range(start_index, len(numbers_dict[str(num)[0]])), numbers_dict[str(num)[0]]):
            if int(str(num)+str(value)) > int(str(value)+str(num)):
                find_index  = index
                break
            else : find_index = index+1
        if find_index == -1 : numbers_dict[str(num)[0]].append(num)
        else : numbers_dict[str(num)[0]].insert(find_index, num)

    if '0' in numbers_dict.keys() and len(numbers_dict.keys()) == 1 : return "0"
    else:
        for numbers_dict_key in sorted(numbers_dict.keys(), reverse=True):
            for num in numbers_dict[numbers_dict_key]:
                answer+=str(num)
        return answer

# print(solution(	[40, 403]))
# print(solution(	[3, 30, 34, 5, 9]))
# print(solution([15,151]))
# print(solution([10, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(solution([412, 41]))
# print(solution([303,30]))
# print(solution([10, 101] ))
# print(solution([1, 11, 111, 1111]))
# print(solution([0, 5, 10, 15, 20]))
print(solution([1000, 0, 5, 99, 100]))

#print(solution([3, 30, 34, 5, 9, 4, 40, 42]))