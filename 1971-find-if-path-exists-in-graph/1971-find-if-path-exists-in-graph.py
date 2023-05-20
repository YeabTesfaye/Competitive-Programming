class UnionFind:

    def __init__(self,n):
        self.parent = list(range(n))
    
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x1,x2):
        p1,p2 = self.find(x1), self.find(x2)

        if p1 != p2:
            self.parent[p1]  = p2
        

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        uf = UnionFind(n)

        for edge in edges:
            uf.union(edge[0], edge[1])
        
        return uf.find(source) == uf.find(destination)
        