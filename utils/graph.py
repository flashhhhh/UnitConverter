from typing import List
from collections import deque

class Graph():
    dictionary: dict[str, int] = {}
    n: int = 0
    adj: List[List[tuple[int, float, float]]] = []
    cost: List[List[tuple[float, float]]] = []
    visited: List[List[bool]] = []

    def __init__(self):
        self.dictionary = {}
        self.n = 0
        self.adj = []
        self.cost = []
        self.visited = []
    
    def add_edge(self, u: str, v: str, multiply: float, add: float = 0.0):
        u = u.lower()
        v = v.lower()

        if u not in self.dictionary:
            self.dictionary[u] = len(self.dictionary)
        if v not in self.dictionary:
            self.dictionary[v] = len(self.dictionary)
        
        # Increase the size of adj and cost if the dictionary has been updated
        while len(self.dictionary) > self.n:
            self.n += 1
            self.adj.append([])
            self.cost.append([0.0 for _ in range(self.n)])
        
        self.adj[self.dictionary[u]].append((self.dictionary[v], multiply, add))
        self.adj[self.dictionary[v]].append((self.dictionary[u], 1.0 / multiply, -add / multiply))
    
    def build(self):
        self.cost = [[[0.0, 0.0] for _ in range(self.n)] for _ in range(self.n)]
        self.visited = [[False for _ in range(self.n)] for _ in range(self.n)]

        for i in range(self.n):
            q = deque([i])

            self.cost[i][i] = [1.0, 0.0]
            self.visited[i][i] = True

            while q:
                u = q.popleft()
                for v, multiply, add in self.adj[u]:
                    if not self.visited[i][v]:
                        self.cost[i][v] = [self.cost[i][u][0] * multiply, self.cost[i][u][1] * multiply + add]
                        self.visited[i][v] = True
                        q.append(v)
    
    def query(self, u: str, v: str) -> float:
        u = u.lower()
        v = v.lower()
        
        return self.cost[self.dictionary[u]][self.dictionary[v]]