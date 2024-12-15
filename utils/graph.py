from typing import List
from collections import deque

class Graph():
    dictionary: dict[str, int] = {}
    n: int = 0
    adj: List[List[tuple[int, float]]] = []
    cost: List[List[float]] = []

    def __init__(self):
        self.dictionary = {}
        self.n = 0
        self.adj = []
        self.cost = []
    
    def add_edge(self, u: str, v: str, w: float):
        if u not in self.dictionary:
            self.dictionary[u] = len(self.dictionary)
        if v not in self.dictionary:
            self.dictionary[v] = len(self.dictionary)
        
        # Increase the size of adj and cost if the dictionary has been updated
        while len(self.dictionary) > self.n:
            self.n += 1
            self.adj.append([])
            self.cost.append([0.0 for _ in range(self.n)])
        
        self.adj[self.dictionary[u]].append((self.dictionary[v], w))
        self.adj[self.dictionary[v]].append((self.dictionary[u], 1.0 / w))
    
    def build(self):
        self.cost = [[0.0 for _ in range(self.n)] for _ in range(self.n)]

        for i in range(self.n):
            q = deque([i])
            self.cost[i][i] = 1.0
            while q:
                u = q.popleft()
                for v, w in self.adj[u]:
                    if self.cost[i][v] == 0:
                        self.cost[i][v] = self.cost[i][u] * w
                        q.append(v)
    
    def query(self, u: str, v: str) -> float:
        if u not in self.dictionary or v not in self.dictionary:
            return -1.0
        
        return self.cost[self.dictionary[u]][self.dictionary[v]] if self.cost[self.dictionary[u]][self.dictionary[v]] != 0 else -1.0