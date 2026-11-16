class Solution:
    def generate(self,n,k,sub,ans,i):
        if len(sub) == k:
            ans.append(sub[:])
            return 
        
        if i == n or  (len(sub)+n-i) < k:
            return
        
        sub.append(i+1)
        self.generate(n,k,sub,ans,i+1)
        sub.pop()
        self.generate(n,k,sub,ans,i+1)

        
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.generate(n,k,[],ans,0)
        return ans