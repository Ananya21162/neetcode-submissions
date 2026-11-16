class Solution:
    def dfs(self,i,adjList,prev,visited,hasCycle):
        if i in visited:
            hasCycle[0] = True
            return
        visited.add(i)
        for c in adjList[i]:
            if c != prev:
                self.dfs(c,adjList,i,visited,hasCycle)
        return
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = [[] for _ in range(n)]
        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        hasCycle = [False]
        visited = set()
        self.dfs(0,adjList,None,visited,hasCycle)
        if hasCycle[0]:
            return False
        for i in range(n):
            if i not in visited:
                return False
                
        return True
