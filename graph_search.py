

class Graph:
    def __init__(self):
        self.graph = {}


    def dfs(self, source):
        visited = [False] * len(self.graph)
        self._dfs(source, visited)
        
    
    def _dfs(self, source, visited):
        visited[source] = True

        for i in self.graph[source]:
            if visited[i] == False:
                self._dfs(i, visited)


    def bfs(self, source):
        visited = [False] * len(self.graph)

        queue = [] 

        queue.append(source)
        visited[source] = True
        
        while queue:
            queue.pop(0)

            for i in self.graph[source]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    
                

            
