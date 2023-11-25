from collections import deque
def add_node(v):
    global node_count
    if v in node:
        print(v, "Already available")
    else:
        node_count += 1
        node.append(v)
        for row in graph:
            row.append(0)
        tem = []
        for i in range(node_count):
            tem.append(0)
        graph.append(tem)


def add_edge(v1, v2):
    if v1 not in node:
        print("Node", v1, "not available")
    elif v2 not in node:
        print("Node", v2, "not available")
    else:
        x = node.index(v1)
        y = node.index(v2)
        graph[x][y] = 1
        graph[y][x] = 1


def print_node(graph):
    global node_count
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j], end=" ")
        print()
        
def DFS(start_node, visited):
    if start_node  not in node:
        print("np")
        return
    visited[node.index(start_node)] = True
   
    print(start_node, end=" ")
   
    for i in range(node_count):
        if graph[node.index(start_node)][i] ==1 and not visited[i]:
            DFS(node[i], visited)
           
def BFS(start_node, visited):
    if start_node not in node:
        print("No")
        return
    queue = deque()
    queue.append(start_node)
   
    while queue:
        current = queue.popleft()
        print(current, end=" ")
        visited[node.index(current)]  = True
       
        for i in range(node_count):
            if graph[node.index(current)][i] == 1 and not visited[i]:
                queue.append(node[i])
                visited[i] = 1
                

visited = []
node = []
graph = []
node_count = 0
add_node("A")
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("M")	
add_edge("A", "B")
add_edge("A", "C")
add_edge("B", "C")
add_edge("C", "D")
add_edge("D", "f")

print()
print(node)
print(graph)

visited = [False]*node_count
DFS("A", visited)
print()
BFS("A", visited)

