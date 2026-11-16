class Solution:
    def dfs(self,i,adjList,visited,hasCycle):
        if i in visited:
            hasCycle[0] = True
            return
        if adjList[i] == []:
            return
        visited.add(i)
        for c in adjList[i]:
            self.dfs(c,adjList,visited,hasCycle)
        visited.remove(i)
        adjList[i] = []
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adjList[a].append(b)
        hasCycle = [False]
        for i in range(numCourses):
            visited = set()
            self.dfs(i,adjList,visited,hasCycle)
            if hasCycle[0]:
                return False
        return True
