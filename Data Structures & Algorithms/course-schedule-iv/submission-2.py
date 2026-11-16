class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        preq_map = {c:[] for c in range(numCourses)}
        for preq,c in prerequisites:
            preq_map[c].append(preq)
        all_preq = {}# list of hashset
        
        def dfs(i):
            if i not in all_preq:
                all_preq[i] = set()
                for p in preq_map[i]:
                    all_preq[i] |= dfs(p)
                all_preq[i].add(i)
            return all_preq[i]
                    
        for i in range(numCourses):
           
            dfs(i)
            
        ans = []
        for u,v in queries:
            if u in all_preq[v]:
                ans.append(True)
            else:
                ans.append(False)
        return ans