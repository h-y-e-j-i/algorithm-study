def solution(numbers):
    numbers.sort()
    numbers = list(map(str, numbers))
    answer = ''
    numbers_dict = dict()
    for num in numbers:
        if num[0] not in numbers_dict.keys():
            numbers_dict[num[0]] = list()


        find_index = -1
        for index, value in zip(range(len(numbers_dict[num[0]])), numbers_dict[num[0]] ):
            if len(value) == 1 : value_prefix = value+value
            else : value_prefix = value[0:2]
            
            if len(num) == 1 : num_prefix = num+num
            else : num_prefix = num[0:2]
            
            if str(num_prefix) < str(value_prefix):
                pass
            elif int(num+str(value)) > int(str(value)+num) :
                find_index  = index
                break
            else : find_index = index+1
        if find_index == -1 : numbers_dict[num[0]].append(num)
        else : numbers_dict[num[0]].insert(find_index, num)

    if '0' in numbers_dict.keys() and len(numbers_dict.keys()) == 1 : return "0"
    else:
        for numbers_dict_key in sorted(numbers_dict.keys(), reverse=True):
            for num in numbers_dict[numbers_dict_key]:
                answer+=str(num)
        return answer