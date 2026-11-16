class Solution:
    def dfs(self,i,visited,preq_map,path,order,possible):
        if not possible[0]:
            return
        if i in path:
            possible[0] = False
            return
        if visited[i]:
            return
        visited[i] = True
        
        path.add(i)
        if len(preq_map[i]) == 0:
            order.append(i)
            path.remove(i)
            return
        for preq in preq_map[i]:
            
            self.dfs(preq,visited,preq_map,path,order,possible)
        order.append(i)
        preq_map[i] = []
        path.remove(i)

    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        preq_map = {}
        for i in range(n):
            preq_map[i] = []
        for c,preq in prerequisites:
            preq_map[c].append(preq)
        visited = [False]*n
        path = set()
        order = []
        possible = [True]
        for i in range(n):
            if not visited[i]:
                self.dfs(i,visited,preq_map,path,order,possible)
                if not possible[0]:
                    return []
        return order