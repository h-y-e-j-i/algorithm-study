def solution(clothes):
    answer = 0
    clothes_dict = dict()

    for clothes_name, clothes_type in clothes:
        if clothes_type not in clothes_dict.keys():
            clothes_dict[clothes_type] = list()
        clothes_dict[clothes_type].append(clothes_name)

    clothes_count = [0 for _ in range(len(clothes_dict.keys()))]
    index = 0
    for clothes_type in clothes_dict.keys():
        clothes_count[index] = len(clothes_dict[clothes_type])
        index += 1
    
    for clothes_count_index in range(len(clothes_count)):
        clothes_match_count = clothes_count[clothes_count_index]
        for target_clothes_count_index in range(clothes_count_index+1, len(clothes_count)):
            clothes_match_count *= (clothes_count[target_clothes_count_index]+1)
        answer += clothes_match_count
    
    return answer

print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))