# https://programmers.co.kr/learn/courses/30/lessons/92341

import math

def solution(fees, records):
    answer = []
    basic_time, basic_fee, unit_time, unit_fee = fees
    car_dict = dict()
    
    for record in records:
        car_time, car_number, car_status = record.split()
        if car_number not in car_dict.keys():
            car_dict[car_number] = list()
        car_dict[car_number].append(car_time)

    car_numbers = list(car_dict.keys())
    car_numbers.sort()

    for car_number in car_numbers:
        if len(car_dict[car_number])%2 == 1: car_dict[car_number].append('23:59')

        parking_time = 0

        for car_index in range(len(car_dict[car_number])//2):
            in_hour, in_minute = list(map(int, car_dict[car_number][car_index*2].split(":")))
            out_hour, out_minute = list(map(int, car_dict[car_number][car_index*2+1].split(":")))
            parking_time += (out_hour-in_hour)*60 + (out_minute-in_minute)
        
        if parking_time <= basic_time : answer.append(basic_fee)
        else:
            answer.append(basic_fee+math.ceil((parking_time-basic_time)/unit_time)*unit_fee)
    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))