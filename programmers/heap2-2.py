def solution(jobs):
    wait_jobs_list = list()
    sum_all_job_run_time = 0
    current_time = 0

    jobs_list = list()
    jobs.sort(key=lambda x:(x[0], x[1]))
    for start_time, run_time in jobs:
        jobs_list.append([start_time-jobs[0][0], run_time])
    #jobs_list.sort(key=lambda x:(x[0], x[1]))

    while jobs_list or wait_jobs_list:        
        wait_jobs_list.sort(key=lambda x: (x[0], x[2]))
        if wait_jobs_list:
            run_time, all_run_time, start_time = wait_jobs_list.pop(0)   
            sum_all_job_run_time += all_run_time
        else:
            start_time, run_time = jobs_list.pop(0)
            sum_all_job_run_time += run_time
        
        current_time += run_time

        for index in range(len(wait_jobs_list)):
            wait_jobs_list[index][1] += run_time

        filter_jobs_list = list(filter(lambda x : x[0]<=current_time, jobs_list))

        if filter_jobs_list:
            for wait_start_time,wait_run_time in filter_jobs_list:
                jobs_list.remove([wait_start_time, wait_run_time])
                wait_jobs_list.append([wait_run_time, wait_run_time+current_time-wait_start_time, wait_start_time,])
        elif not filter_jobs_list and jobs_list:
            wait_start_time, wait_run_time = jobs_list.pop(0)
            wait_jobs_list.append([wait_run_time, wait_run_time, wait_start_time])
    
    answer = int(sum_all_job_run_time/len(jobs))
    return answer   
            
# print(solution(	[[0, 3], [1, 9], [2, 6]]))
# print(solution( [[15, 34], [15, 2], [20, 47], [24, 10], [26, 1], [28, 39], [35, 43], [37, 5], [43, 20], [47, 22]]))
#print(solution([[0, 3], [4, 4], [5, 3], [4, 1]]))                
# print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))
# print(solution([[1000, 1000]]))
print(solution(	[[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]))
# print(solution([[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]]))

