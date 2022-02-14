import heapq

def solution(jobs):
    answer = 0
    wait_number_list = list()

    heap = list()
    for number, time in jobs:
        wait_number_list.append(number)
        heapq.heappush(heap, [time, number])
    
    wait_time_list = [ 0 for _ in range(len(wait_number_list))]

    while heap:
        time, number = heapq.heappop(heap)
        for _ in range(time):
            for wait_number in wait_number_list:
                wait_time_list[wait_number] += 1
        wait_number_list.remove(number)

    delay_sum = 0
    for i in range(len(wait_time_list)): 
        delay_sum += i

    answer = (sum(wait_time_list)-delay_sum)/len(wait_time_list)
    return answer

print(solution([[0, 3], [1, 9], [500, 6]]))


