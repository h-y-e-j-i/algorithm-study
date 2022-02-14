def solution(array, commands):
    answer = []
    for i, j, k in commands:
        part_array = sorted(array[i-1:j])
        answer.append(part_array[k-1])
    return answer