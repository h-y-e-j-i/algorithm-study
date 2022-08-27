# https://www.acmicpc.net/problem/2941
# 크로아티아 알파벳
import sys

input_str = [s for s in sys.stdin.readline().strip()]
croatia = ["c=", "c-", "d-", "lj", "nj", "s=", "z="]

count = len(input_str)
idx = 0

while idx < len(input_str[:-1]):
    if idx<len(input_str)-2 and input_str[idx]+input_str[idx+1]+input_str[idx+2]=="dz=":
        count -= 2
        idx += 3
    elif input_str[idx]+input_str[idx+1] in croatia:
        count -= 1
        idx += 2
    
    else : idx += 1
    
print(count)


