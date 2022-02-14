def solution(numbers):
    answer = ''
    numbers_dict = dict()
    for num in numbers:
        num = str(num)
        if num[0] not in numbers_dict.keys():
            numbers_dict[num[0]] = list()
        if len(num) == 1:
            numbers_dict[num[0]].append([str(int(num)*111), int(num)])
        elif len(num) == 2:
            if int(num[0])<int(num[1]):numbers_dict[num[0]].append([num+num[1], int(num)])
            else : numbers_dict[num[0]].append([num+num[0], -int(num)])
        elif len(num)==4:
            numbers_dict[num[0]].append([str(int(int(num)/10)), -int(num)])
        else:
            numbers_dict[num[0]].append([num, int(num)])
        # temp = int(num)*pow(10, 3-len(num))
        # for add_zero in range(3-len(num)):
        #     temp += int(num[0])*pow(10, add_zero)
        # numbers_dict[num[0]].append([str(temp), int(num)])
   
    for numbers_dict_key in sorted(numbers_dict.keys(), reverse=True):
        numbers_dict[numbers_dict_key] = sorted(numbers_dict[numbers_dict_key], reverse=True)
        for _, number_value in numbers_dict[numbers_dict_key] : 
            answer+=str(abs(number_value))
            
    if list(set(answer)) == ['0']:
        answer = "0"
    return answer


#print(solution(["3", "30", "344" , "352", "334"]))
print(solution([15,151]))
print(solution([10, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution([412, 41]))
print(solution([303,30]))
print(solution([10, 101] ))
print(solution([1, 11, 111, 1111]))
print(solution([0, 5, 10, 15, 20]))
print(solution([1000, 0, 5, 99, 100]))
# print(solution(["3", "30", "34", "5", "9"]))
# print(sorted(["3", "30", "34", "342", "31"]))
