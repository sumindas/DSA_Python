from collections import deque
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, src, dest):
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)

    def print_graph(self):
        for vertex in range(self.num_vertices):
            print(f"Adjacency list of vertex {vertex}: ", end="")
            for neighbor in self.adj_list[vertex]:
                print(f"{neighbor} -> ", end="")
            print("null")

    def bfs(self, start_vertex):
        visited = [False] * self.num_vertices
        queue = deque()

        visited[start_vertex] = True
        queue.append(start_vertex)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbor in self.adj_list[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

    def dfs(self, start_vertex):
        visited = [False] * self.num_vertices

        def dfs_recursive(vertex):
            visited[vertex] = True
            print(vertex, end=" ")

            for neighbor in self.adj_list[vertex]:
                if not visited[neighbor]:
                    dfs_recursive(neighbor)

        dfs_recursive(start_vertex)
        
    def is_connected(self,start,end):
        visited = [False] * self.num_vertices
        queue = deque()
        visited[start] = True
        queue.append(start)
        while queue:
            
            current = queue.popleft()
            if current == end:
                return True
            
            for neighbour in self.adj_list[current]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)
    
        return False

       
        


graph = Graph(5)


graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)


graph.print_graph()
print("DFS")
graph.dfs(0)
print("\nBFS")
graph.bfs(0)
print()
print(graph.is_connected(0,2))
