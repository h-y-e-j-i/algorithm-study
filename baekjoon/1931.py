# https://www.acmicpc.net/problem/1931
# 회의실 배정
import sys

n = int(sys.stdin.readline().strip())
start_time_dict = dict()
same_time_dict = dict()
total_time = 0

for _ in range (n):
    start_time, end_time = list(map(int, sys.stdin.readline().strip().split(" ")))
    if start_time not in same_time_dict.keys():
        same_time_dict[start_time] = 0

    if start_time not in start_time_dict.keys():
        if start_time == end_time:
            same_time_dict[start_time] += 1
        else : 
            start_time_dict[start_time] = [[start_time, end_time]]
    else:
        tmp_start_time, tmp_end_time = start_time_dict[start_time][0]
        if start_time == end_time:
            same_time_dict[start_time] += 1
        elif tmp_end_time > end_time:
            start_time_dict[start_time] = [[start_time, end_time]]
        
    
    if total_time < end_time : total_time = end_time

meeting_count = 0
on_meeting = False
t = min(start_time_dict.keys())
end_time = float("inf")
while t <= total_time:
    if t in start_time_dict.keys():
        start_time, end_time = start_time_dict[t][0]
    # 중간에 더 짧은 미팅이 있는 경우
    # 1. 바로 끝나는 미팅만 있는 경우
    if on_meeting and t in same_time_dict.keys() and same_time_dict[t] > 0 and t not in start_time_dict.keys() and t<end_time:
        meeting_count += same_time_dict[t]
        same_time_dict[t] = 0    
        on_meeting = False
        #print(f"[{t} {t}]")
        t += 1
    # 2. 바로 끝나지 않는 미팅도 있는 경우
    elif on_meeting and t in start_time_dict.keys() and end_time<current_end_time:
        current_start_time = start_time
        current_end_time = end_time
        t += 1
    # 미팅이 시작하는 경우
    ## 1. 시작하자마자 끝나는 미팅만 있는 경우
    elif not on_meeting and t in same_time_dict.keys() and same_time_dict[t] > 0 and t not in start_time_dict.keys():
        meeting_count += same_time_dict[t]
        t += 1
        same_time_dict[current_start_time] = 0
    ## 2.시작하자마자 끝나지 않은 미팅도 있는 경우
    elif not on_meeting and t in start_time_dict.keys():
        current_start_time = start_time
        current_end_time = end_time
        on_meeting = True
        t += 1
        # 미팅이 끝나는 경우
    elif on_meeting and current_end_time == t :
        meeting_count += len(start_time_dict[current_start_time])
        meeting_count += same_time_dict[current_start_time]
        same_time_dict[current_start_time] = 0
        on_meeting = False
    else:
        t += 1

print(meeting_count)
    




    