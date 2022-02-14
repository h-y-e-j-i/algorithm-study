
# https://www.acmicpc.net/problem/15486
import sys

work_day = int(sys.stdin.readline().strip())
consult = [[0, 0]]

# f : 해당 날짜를 선택했을 때 얻을 수 있는 최대의 금액
# g : 해당 날짜 이후 중에서 선택했을 때의 최대 금액
f = [-1]*(work_day+1)
g = [-1]*(work_day+1)

for d in range(1, work_day+1):
    consult_day, money = map(int, sys.stdin.readline().strip().split())
    consult.append([consult_day, money]) # Ti, Pi


def DP(N):
    for i in range(N, 0, -1):
        # 해당 날짜+상담 날짜가 마지막날+1이라면
        # 해당 날짜를 선택했을 때(f) 얻을 수 있는 최대의 돈은 해당 날짜의 금액
        if i+consult[i][0] == work_day+1 and f[i]==-1: 
            f[i] = consult[i][1]

            if i+1>work_day : g[i] = f[i]
            else:  g[i] = max(f[i], g[i+1])
        # 해당 날짜+상담 날짜가 마지막날+1보다 크다면
        # 해당 날짜를 선택했을 때(f) 얻을 수 있는 최대의 돈은 0
        elif i+consult[i][0] > work_day+1 and f[i]==-1: 
            f[i] = 0

            if i+1>work_day : g[i] = f[i]
            else:  g[i] = max(f[i], g[i+1])
        else:
        # 마지막날+1보다 작으면 
        # 해당 날짜에 받을 수 있는 금액 + 해당 날짜 이후 중에서 선택했을 때의 최대 금액(g)
            f[i] = consult[i][1]+g[i+consult[i][0]]
            g[i] = max(f[i], g[i+1])     
                
DP(work_day)
print(max(f))