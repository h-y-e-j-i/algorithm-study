def BFS(graph, start_node, end_node):
    queue = list()
    visited = list()
    node_distance = dict()
    step = 0

    queue.append(start_node)
    node_distance[start_node] = 0
    while queue:
        node = queue.pop()
        if node not in visited:
            visited.append(node)
            if node == end_node:
                step = max(node_distance.values())
            for next_node in graph[node]:
                if next_node not in visited and next_node not in queue:
                    node_distance[next_node] = node_distance[node]+1
                    queue.append(next_node)
    return step

def make_graph(words):
    graph = dict()
    for word in words:
        graph[word] = list()
        for target_word in words:
            if word != target_word:                
                count = 0
                for ch_index in range(len(word)):
                    if word[ch_index] != target_word[ch_index] : count+=1
                if count == 1 : graph[word].append(target_word)

    return graph
                
                    
def solution(begin, target, words):
    words.append(begin)
    graph = make_graph(words)
    answer = BFS(graph, begin, target)
    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]	))