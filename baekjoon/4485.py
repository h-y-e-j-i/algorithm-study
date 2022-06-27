# https://www.acmicpc.net/problem/4485
# 녹색 옷 입은 애가 젤다지?
# https://www.youtube.com/watch?v=acqm9mM1P6o&t=979s
# 다익스트라 알고리즘

import sys
import heapq


def dijkstra(start, distance, graph):
    q = list()

    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))

    while q : # 큐가 비어있지 않으면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dis, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있는 노드라면 무시
        if distance[now] < dis : continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for next_node, next_cost  in graph[now]:
            cost = dis + next_cost
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

    return distance

problem_number = 1

n = int(sys.stdin.readline())

while n!=0:
    # 시작 노드 번호
    start = 0
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [float("inf")] * (n*n) 
    # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
    graph = [[] for _ in range(n*n)] # 

    # 입력받기
    cave = list()
    for _ in range(n):
        cave.append(list(map(int, sys.stdin.readline().strip().split(" "))))

    # 동굴의 사방에 있는 node를 graph 배열에 넣음
    # 동굴은 2차원 배열, graph는 1차원 배열이므로 둘 사이의 다음과 같은 식으로 inddex를 변환
    for i in range(n):
        for j in range(n):
            node = i*n+j
            if i-1>=0 : graph[node].append((n*(i-1)+j, cave[i-1][j]))
            if i+1<n : graph[node].append((n*(i+1)+j, cave[i+1][j]))
            if j-1>=0 : graph[node].append((n*i+(j-1), cave[i][j-1]))
            if j+1<n : graph[node].append((n*i+(j+1), cave[i][j+1]))

    # 최단거리 찾아서 최종 최단거리 테이블 구하기
    result_distance = dijkstra(start, distance, graph)

    # 처음 시작 노드 비용 + 마지막 노드 비용
    print(f"Problem {problem_number}: {result_distance[-1]+cave[0][0]}")

    n = int(sys.stdin.readline())
    problem_number += 1




