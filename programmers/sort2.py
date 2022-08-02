def solution(numbers):
    numbers.sort()
    numbers = list(map(str, numbers))
    answer = ''
    numbers_dict = dict()
    for num in numbers:
        if num[0] not in numbers_dict.keys():
            numbers_dict[num[0]] = list()
        
        sort_num = num
        while len(sort_num) < 4:
            sort_num += num
        sort_num = sort_num[0:4]

        numbers_dict[num[0]].append([sort_num, num])

    if '0' in numbers_dict.keys() and len(numbers_dict.keys()) == 1 : return "0"
    else:
        for numbers_dict_key in sorted(numbers_dict.keys(), reverse=True):
            for _, num in sorted(numbers_dict[numbers_dict_key], reverse=True):
                answer+=str(num)
        return answer

# print(solution([1, 11, 111, 1111]))
# print(solution([0, 5, 10, 15, 20]))
print(solution([1000, 0, 5, 99, 100]))

# print(solution([3, 30, 34, 5, 9, 4, 40, 42]))