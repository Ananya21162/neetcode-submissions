class Solution:
    def dfs(self,i,adjList,visited):
        if i in visited:
            return
        visited.add(i)
        for c in adjList[i]:
            self.dfs(c,adjList,visited)
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        visited = set()
        adjList = defaultdict(list)
        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        for i in range(n):
            if i not in visited:
                self.dfs(i,adjList,visited)
                count += 1
        return count