class Solution:
    def generate(self,i,k,n,ans,sub):
        if k == 0:
            ans.append(sub[:])
            return
        if i == n+1 or k < 0:
            return
        sub.append(i)
        self.generate(i+1,k-1,n,ans,sub)
        sub.pop()
        self.generate(i+1,k,n,ans,sub)
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.generate(1,k,n,ans,[])
        return ans
        