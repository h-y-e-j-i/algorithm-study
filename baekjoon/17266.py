import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
locations = list(map(int, sys.stdin.readline().strip().split(" ")))

intervals = [locations[0]]
for i in range(1, m):
    intervals.append(locations[i]-locations[i-1])
intervals.append(n-locations[m-1])

max_interval = max(intervals)//2+max(intervals)%2
if  intervals[0] > max_interval or intervals[-1] > max_interval:
    print(max([intervals[0], intervals[-1]]))
else:
    print(max_interval)