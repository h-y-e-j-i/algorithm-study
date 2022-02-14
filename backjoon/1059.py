import sys
answer = 0

loop = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
N = int(sys.stdin.readline())

num_list = sorted(num_list)
index = 0

for num in num_list:
    if num >= N:
        index = num_list.index(num)
        break

if N in num_list or index == len(num_list)-1:
    print(0)
elif index == 0:
    for i in range(1, num_list[index]):
        for j in range(N, num_list[index]):
            if i!=j:answer += 1

    print(answer)
else:
    for i in range(num_list[index-1]+1, N+1):
        for j in range(N, num_list[index]):
            if i!=j:answer += 1
    
    print(answer)

