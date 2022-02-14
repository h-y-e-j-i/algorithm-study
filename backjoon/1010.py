import sys
loop = int(input())
answers = list()

for _ in range(loop):
    result = 1
    west, east = map(int, sys.stdin.readline().split())
    
    count = 0
    for num in range(east, 0, -1):
        count += 1
        result = result*num
        if count == west : break
        
    
    for num in range(1, west+1):
        result = result//num

    print(int(result))


