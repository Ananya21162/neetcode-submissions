class Solution:
    def dfs(self,i,adjList,path,prev,cycleStart,visited):
        if visited[i]:
            cycleStart[0] = i
            return True
        visited[i] = True
        for c in adjList[i]:
            if c != prev:
                if self.dfs(c,adjList,path,i,cycleStart,visited):
                    if cycleStart[0] != -1:
                        path.add(i)
                    if i == cycleStart[0]:
                        cycleStart[0] = -1
                    return True
        return False
                    
       
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
       
        adjList = defaultdict(list)
        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
     
        path = set()
        visited = [False]*(len(adjList)+1)
        self.dfs(1,adjList,path,None,[-1],visited)
       
        for u,v in reversed(edges):
            if u in path and v in path:
                return [u,v]
        return []
