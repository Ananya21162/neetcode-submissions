class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]
        size = [1] * (n + 1)

        def findParent(u):
            if parent[u] != u:
                parent[u] = findParent(parent[u])
            return parent[u]

        def union(u, v):
            pu = findParent(u)
            pv = findParent(v)

            if pu == pv:
                return False  # cycle detected

            # union by size
            if size[pu] >= size[pv]:
                parent[pv] = pu
                size[pu] += size[pv]
            else:
                parent[pu] = pv
                size[pv] += size[pu]

            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
