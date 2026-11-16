class Solution:
    def dfs(self, i, adjDict,visited):
        # if len(adjDict[i]) == 0:
        #     return
        visited.add(i)
        for c in adjDict[i]:
            if c not in visited:
                self.dfs(c,adjDict,visited)
            adjDict[i] = adjDict[i] | adjDict[c]
        return
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjDict = defaultdict(set)
        for a,b in prerequisites:
            adjDict[b].add(a)
        visited = set()
        for i in range(numCourses):
            if i not in visited:
                self.dfs(i,adjDict,visited)
        print(adjDict)
        ans = []
        for query in queries:
            a,b = query[0], query[1]
            if a in adjDict[b]:
                ans.append(True)
            else:
                ans.append(False)
        return ans