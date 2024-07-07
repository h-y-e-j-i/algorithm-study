import sys

switch_cnt = int(sys.stdin.readline().strip())
switch = sys.stdin.readline().strip().split(" ")
student_cnt = int(sys.stdin.readline().strip())

for _ in range(student_cnt):
    sex, num = sys.stdin.readline().strip().split(" ")
    sex, num = int(sex), int(num)

    if sex == 1:
        for i in range(0, switch_cnt):
            if (i+1)%num == 0:
                if switch[i] == '1':
                    switch[i] = '0'
                else:
                    switch[i] = '1'
    else:
        inverse_interval = 1

        if ((switch_cnt-1)-(num-1)) >= (num-1):
            interval = num-1
        else:
            interval = (switch_cnt-1)-(num-1)

        if switch[num-1] == '1':
            switch[num-1] = '0'
        else:
            switch[num-1] = '1'
        


        for i in range(num, num+interval):
            if switch[i] == switch[i-inverse_interval-1]:
                if switch[i] == '1':
                    switch[i] = '0'
                else:
                    switch[i] = '1'

                if switch[i-inverse_interval-1] == '1':
                    switch[i-inverse_interval-1] = '0'
                else:
                    switch[i-inverse_interval-1] = '1'
                inverse_interval += 2
            else:
                break


max_line = switch_cnt // 20 if switch_cnt%20 == 0 else switch_cnt%20+1

for i in range(max_line):
    print(' '.join(switch[20*i:20*(i+1)]))