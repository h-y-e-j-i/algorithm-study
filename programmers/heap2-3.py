def solution(jobs):
    run_jobs_list = list()
    wait_jobs_list = list()
    sum_run_time = 0
    current_run_time = 0

    for start_time, run_time in jobs:
        wait_jobs_list.append([start_time, run_time])
    
    wait_jobs_list.sort(key = lambda x:(x[0], x[1]))

    while wait_jobs_list or run_jobs_list:
        if wait_jobs_list:
            run_time, start_time, wait_time = wait_jobs_list.pop(0)
        else:
            run_time, start_time = run_jobs_list.pop(0)

        for t in range(run_time):
            current_run_time += t
            for index in range(len(run_jobs_list)):
                if run_jobs_list[index][0] == current_run_time:
                    run_time, start_time = run_jobs_list.pop(0)
                    wait_jobs_list.append(run_time, start_time, 0)
                else : break

            for index in range(len(wait_jobs_list)):
                wait_jobs_list[index][2] += 1
            
