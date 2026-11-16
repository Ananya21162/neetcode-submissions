class Solution:
    def dfs(self, i, adjList, visited, path):
        if path[i]:      # cycle found
            return False
        if visited[i]:   # already processed safely
            return True

        path[i] = True
        for nei in adjList[i]:
            if not self.dfs(nei, adjList, visited, path):
                return False

        path[i] = False
        visited[i] = True
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adjList[a].append(b)

        visited = [False] * numCourses
        path = [False] * numCourses

        for i in range(numCourses):
            if not visited[i]:
                if not self.dfs(i, adjList, visited, path):
                    return False

        return True
