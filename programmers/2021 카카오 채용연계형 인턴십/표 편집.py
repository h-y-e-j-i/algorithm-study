# https://programmers.co.kr/learn/courses/30/lessons/81303?language=python3
# 표 편집
class Node: 
    def __init__(self, element, next_node=None, previous_node=None):
        self.element = element #다음 데이터 주소 초기값 = None
        self.previous_node = previous_node
        #self.table_previous_node = previous_node
        self.next_node = next_node
        #self.table_next_node = next_node

class DoublyLinkedList:
    def __init__(self):
        self.head = Node('head')

    def find(self, item):
        cur_node = self.head
        while cur_node.element != item:
            cur_node = cur_node.next_node
        return cur_node
    
    def insert(self, item, new):
        new_node = Node(new)
        cur_node = self.find(item)
        
        new_node.next_node = cur_node.next_node
        cur_node.next_node = new_node
        new_node.previous_node = cur_node

    def remove(self, item):
        cur_node = self.find(item)
        cur_node.previous_node.next_node = cur_node.next_node
        #cur_node.previous_node = None

        if cur_node.next_node is not None:
            cur_node.next_node.previous_node = cur_node.previous_node
            cur_node.next_node = None

    def show(self, start_node):
        node_list = list()
        cur_node = self.find(start_node)
        while cur_node.next_node is not None:
            node_list.append(cur_node.element)
            #print(cur_node.element, end='=>')
            cur_node = cur_node.next_node
        #print(cur_node.element)
        node_list.append(cur_node.element)
        return node_list

def solution(n, k, cmd):
    table = DoublyLinkedList()
    remove_node_list = list()


    table.insert('head', 0)
    for idx in range(n-1) :
        table.insert(idx, idx+1)
    table.show(k)

    cur_node = table.find(k)
    for c in cmd:        
        if c[0]=='D': # 아래로 이동
            _, move_row_num = c.strip().split(" ")
            move_row_num = int(move_row_num)

            for _ in range(move_row_num):
                cur_node = cur_node.next_node
        elif c[0]=='U': # 위로 이동
            _, move_row_num = c.strip().split(" ")
            move_row_num = int(move_row_num)

            for _ in range(move_row_num):
                cur_node = cur_node.previous_node
        elif c[0]=='C' : # 삭제
            if cur_node.next_node==None : # 마지막 노드인 경우
                cur_node = cur_node.previous_node
                remove_node_list.append(cur_node.next_node.element)
                table.remove(cur_node.next_node.element)
            else:
                cur_node = cur_node.next_node
                remove_node_list.append(cur_node.previous_node.element)
                table.remove(cur_node.previous_node.element)
        elif c[0]=='Z' : # 복구
            is_insert = False
            re_node_element = remove_node_list.pop()
            search_node = table.head
            
            while search_node.next_node is not None :
                if search_node.next_node.element > re_node_element:
                    table.insert(search_node.next_node.element,re_node_element)
                    is_insert = True
                    break
                else : search_node = search_node.next_node
            if not is_insert: # 복구해야할 숫자가 가장 높은 숫자라 맨 끝에 추가해야하는 경우
                table.insert(search_node.element,re_node_element)
    
    answer = ['X']*n
    #node_list = table.show('head')

    for node in table.show('head'):
        if node=='head' : pass
        else : answer[node] = 'O'

    return "".join(answer)


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))

