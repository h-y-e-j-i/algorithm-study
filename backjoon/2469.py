import sys

std_count = int(sys.stdin.readline())
std = dict()
for std_id in range(1,std_count+1):
    std[std_id] = list(map(int, sys.stdin.readline().split()))

# std_sorted = sorted(std.items(), key=lambda x:len(x[1]))
# print(std_sorted)

visit = list()
visit_route = list()
visit_route_array = list()
stack = list()

node_level = [-1 for _ in range(std_count+1)] 

time_count = 0

stack.append(1)
node_level[1] += 1

while stack:
    node = stack.pop()
    time_count = node_level[node]
    for next_node in std[node]:
        if node_level[next_node] == -1:
            time_count += 1
            stack.append(next_node)
            node_level[next_node] = time_count




max_level = max(node_level)
print(node_level)


