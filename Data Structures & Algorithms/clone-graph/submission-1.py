class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        valMap = {}
        
        def dfs(n):
            if not n or n.val in valMap:
                return
            valMap[n.val] = Node(val = n.val)
            valMap[n.val].neighbors = []
            for neigh in n.neighbors:
                dfs(neigh)
            return
        
        visited = set()
        def copy(n):
            if not n or n.val in visited:
                return
            visited.add(n.val)
            for neigh in n.neighbors:
                valMap[n.val].neighbors.append(valMap[neigh.val])
                copy(neigh)
            return
        dfs(node)
        copy(node)        
        return valMap[node.val]