import sys

n, k = list(map(int, sys.stdin.readline().strip().split(" ")))
hps = [c for c in sys.stdin.readline().strip()]

eat_cnt = 0
for i in range(n):
    if hps[i] == 'P':
        for j in range(k, 0, -1):
            flag = -1
            if i-j >= 0 and hps[i-j]=='H':
                eat_cnt += 1
                hps[i-j] = 0
                flag = 0 
                break

        if flag == 0:
            pass
        else:
            for j in range(1, k+1, 1):
                if i+j < n and hps[i+j]=='H':
                    eat_cnt += 1
                    hps[i+j] = 0
                    flag = 0 
                    break


print(eat_cnt)