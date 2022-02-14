# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=5&contestProbId=AWJHmLraeEwDFAUH
T = int(input())

for test_case in range(1, T + 1):
    minzy_room, treasure_room = list(map(int, input().split()))
    depart_room, arrive_room = [minzy_room, treasure_room] if minzy_room < treasure_room else [treasure_room, minzy_room]
    # 출발, 도착 방의 좌표
    # 출발, 도착 좌표의 x, y는 모두 1부터 시작
    depart_location, arrive_location = [None, None], [None, None] 
    last_room = 1
    line = 1
    while True:
        # 그 줄의 첫번째 방 번호가 출발 방 번호가 크다면
        # 그 줄이 출방 방의 줄

        # 출발 방의 좌표 구하기
        if last_room >= depart_room and depart_location == [None, None]:
            depart_location = [line, line-(last_room-depart_room)]
        # 도착 방의 좌표 구하기
        if last_room >= arrive_room and arrive_location == [None, None]:
            arrive_location = [line, line-(last_room-arrive_room)]

        # 출발, 도착 방의 좌표를 둘 다 구했다면 while문을 나온다
        if depart_location != [None, None] and arrive_location != [None, None]:
            break
        # 둘 중에 하나도 못구했다면 아래 줄로 이동한다
        else:
            
            line += 1
            last_room += line           
    
    arrive_left_room, arrive_right_room = depart_room, depart_room
    
    for i in range(depart_location[0], arrive_location[0]):
        arrive_left_room += i
        arrive_right_room += (i+1)
    
    # 출방 방에서 양쪽으로 시작해서 도착 방까지의 줄에 도달했을 때,
    # 그 양 쪽 사이에 있다면 시간은 line number의 차이다
    move = arrive_location[0]-depart_location[0]
    
    # 그러나 그 밖의 범위에 있을 때에는
    # 그 양쪽 방에서 가장 가깝게 가는 거리를 구해 더한다.
    if arrive_left_room > arrive_room : move += (arrive_left_room-arrive_room)
    elif arrive_right_room < arrive_room: move += (arrive_room)-arrive_right_room
    
    print(f"#{test_case} {move}")

