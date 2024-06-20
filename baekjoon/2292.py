import sys

n = int(sys.stdin.readline().strip())

min = 1
max = 1
interval = 6
line = 1

while True:
    if min <= n <= max:
        print(line)
        break
    else:
        # if min == 1:
        min_next = max
        max += interval
        min = min_next+1
        # else:
    interval += 6
    line += 1

