from math import ceil

def solution(progresses, speeds):
    answer = []
    release_calc_days = []
    release_final_days = []
    release_final_days_count = []
    
    for i in range(len(speeds)) :
        release_calc_days.append(ceil((100-progresses[i])/speeds[i]))
 
    for i in range(len(release_calc_days)):
        if i == 0:
            release_final_days.append(release_calc_days[i])
            release_final_days_index = 0
            release_final_days_count.append(1)
        else :
            if release_calc_days[i] <= release_final_days[release_final_days_index]:
                release_final_days_count[len(release_final_days_count)-1] += 1
            else:
                release_final_days.append(release_calc_days[i])
                release_final_days_count.append(1)
                release_final_days_index += 1         
    
    answer = release_final_days_count
    
    return answer