# https://www.acmicpc.net/problem/11657
# https://www.youtube.com/watch?v=Ppimbaxm8d8&t=298s
# https://velog.io/@younge/Python-%EC%B5%9C%EB%8B%A8-%EA%B2%BD%EB%A1%9C-%EB%B2%A8%EB%A7%8C-%ED%8F%AC%EB%93%9CBellman-Ford-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98

# 첫째 줄에 도시의 개수 N (1 ≤ N ≤ 500), 버스 노선의 개수 M (1 ≤ M ≤ 6,000)이 주어진다.
num_of_city, num_of_bus_line = list(map(int, input().split()))

# 최소 이동 시간 dict 생성
shortest_travel_time = dict()

# 입력 받은 이동 시간 dict 생성
input_travel_time = dict()

for city in range(1, num_of_city+1):
    # 최소 이동 시간은 무한대로 초기화 
    shortest_travel_time[city] = float('inf')
    # 도착 도시까지의 이동 시간을 담을 출발 도시 dict 생성
    input_travel_time[city] = dict()

# 시작 도시인 1번 도시는 최소 이동거리가 0이다
shortest_travel_time[1] = 0

# 음수 순환 확인
negative_cycle = False

# 둘째 줄부터 M개의 줄에는 버스 노선의 정보 A, B, C (1 ≤ A, B ≤ N, -10,000 ≤ C ≤ 10,000)가 주어진다. 
# A는 시작도시, B는 도착도시, C는 버스를 타고 이동하는데 걸리는 시간이다. 
for _ in range(num_of_bus_line):
    depart_city, arrive_city, travel_time = list(map(int, input().split()))
    # 만약 이미 입력받은 이동 시간이 입력할 이동 시간보다 작다면 pass
    if arrive_city in list(input_travel_time[depart_city].keys()) and input_travel_time[depart_city][arrive_city]<travel_time:
        pass
    else : input_travel_time[depart_city][arrive_city] = travel_time

# 정점의 개수(도시의 개수)만큼 반복하여 갱신
for _ in range(num_of_city):
    for depart_city in input_travel_time.keys():
        for arrive_city in input_travel_time[depart_city]:
            # [출발 도시까지의 최소 이동 시간 + 입력받은 출발 도시에서 도착 도시의 이동 시간]이 [지금까지의 최소 이동 시간]보다 작다면
            # 최소 이동 시간을 갱신한다
            if shortest_travel_time[arrive_city] > shortest_travel_time[depart_city] + input_travel_time[depart_city][arrive_city]:
                shortest_travel_time[arrive_city] = shortest_travel_time[depart_city] + input_travel_time[depart_city][arrive_city]

# 음수 cycle 판별
for depart_city in input_travel_time.keys():
    for arrive_city in input_travel_time[depart_city]:
        # 만약 최종 최소 이동 거리가 [출발 도시까지의 최소 이동 시간 + 입력받은 출발 도시에서 도착 도시의 이동 시간]보다 크다면
        # 음수 cycle이 반복
        if shortest_travel_time[arrive_city] > shortest_travel_time[depart_city] + input_travel_time[depart_city][arrive_city]:
            negative_cycle = True
            break

# 음의 순환이 반복된다면 -1 출력
if negative_cycle : print(-1)
else:
    # 이동 시간만 가져온다
    shortest_travel_time_list = list(shortest_travel_time.values())
    # 시작 도시는 제외한다
    shortest_travel_time_list.pop(0)
    # 이동 시간이 inf인 경우 -1로 출력, 아니면 그대로 출력
    for i in shortest_travel_time_list :
        if i==float('inf') : print(-1)
        else : print(i)
