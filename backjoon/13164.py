import sys

pepole_count, group_count = map(int,sys.stdin.readline().split())
people_array = list(map(int, sys.stdin.readline().split()))

q, r = divmod(pepole_count, group_count)
print(q+1)