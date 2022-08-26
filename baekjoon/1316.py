# https://www.acmicpc.net/problem/1316
# 그룹 단어 체커
import sys

n = int(sys.stdin.readline().strip())
count = 0

for _ in range(n):
    input_str = [s for s in sys.stdin.readline().strip()]

    ch_list = list()
 
    flag = 0

    for idx, s in enumerate(input_str):
        if input_str[idx] not in ch_list:
            ch_list.append(input_str[idx])
        elif input_str[idx] in ch_list and input_str[idx]!=input_str[idx-1]:
            flag = -1
    
    if flag == 0 : count+=1

print(count)
    

