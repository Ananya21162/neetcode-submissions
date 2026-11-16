class Solution:
    def dfs(self,i,adjList,visited,hasCycle, res,courses):
        if i in visited:
            hasCycle[0] = True
            return
        if adjList[i] == []:
            if not courses[i]:
                res.append(i)
                courses[i] = True
            return
        visited.add(i)
        courses[i] = True
        for c in adjList[i]:
            self.dfs(c,adjList,visited,hasCycle,res,courses)
        visited.remove(i)
        adjList[i] = []
        res.append(i)

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(numCourses)]
        for item in prerequisites:
            adjList[item[0]].append(item[1])
        res = []
        hasCycle = [False]
        courses = [False for _ in range(numCourses)]
        for i in range(numCourses):
            visited = set()
            self.dfs(i,adjList,visited,hasCycle, res,courses)
            if hasCycle[0]:
                return []
        return res