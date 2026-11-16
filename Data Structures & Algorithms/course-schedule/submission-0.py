class Solution:
    def bfs(self,i,visited,path,prereq_map):
        visited[i] = True
        path.add(i)
        q = deque([i])
        while q:
            c = q.popleft()
            for preq in prereq_map[c]:
                if preq in path:
                    return False
                if not visited[preq]:
                    visited[preq] = True
                    q.append(preq)
        return True
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [False] * numCourses
        prereq_map = {}
        for i in range(numCourses):
            prereq_map[i] = []
        for c, preq in prerequisites:
            
            prereq_map[c].append(preq)
        # print(visited,prereq_map)
        for i in range(numCourses):
            path = set() # to detect cycles, if the same node is present in path, we return False
            # print(i)
            if not visited[i]:
                if not self.bfs(i,visited,path,prereq_map):
                    return False
        return True
    
