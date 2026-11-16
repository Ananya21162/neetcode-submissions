class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        rank = [0]*(n+1)
        parent = [i for i in range(n+2)]
        def findParent(n):
            # path compression
            if parent[n] == n:
                return n
            parent[n] = findParent(parent[n])
            return parent[n]

        def unionbyRank(n1,n2):
            p1 = findParent(n1)
            p2 = findParent(n2)
            if p1 == p2:
                return False
            # do the union of the edge
            if rank[p1] > rank[p2]:
                parent[p2] = p1
            elif rank[p2] > rank[p1]:
                parent[p1] = p2
            else: 
                parent[p2] = p1
                rank[p1] += 1

            return True
        
        for u, v in edges:
            if not unionbyRank(u,v):
                return [u,v]
            