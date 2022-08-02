# https://programmers.co.kr/learn/courses/30/lessons/72411?language=python3
# 메뉴 리뉴얼
import itertools

def BFS(graph, start_node)
    queue = list()
    visited = list()

    queue.append(start_node)
    while queue:
        node = queue.pop()
        if node not in visited:
            queue.append(graph[node])


def solution(orders, course):
    menu = dict()

    for cumstomer, order in enumerate(orders):
        for o in order:
            if o not in menu.keys():
                menu[o] = list()
            menu[o].append(cumstomer)
        
    for menu_count in course:
        



        


    answer = []
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))