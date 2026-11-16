class Solution:
    def generate(self,open,close,n,ans, sub):
        if open == n and close == n:
            ans.append("".join(sub[:]))
        
        if open < n:
            sub.append("(")
            self.generate(open+1,close,n,ans,sub)
            sub.pop()
        if open > close:
            sub.append(")")
            self.generate(open,close+1,n,ans,sub)
            sub.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.generate(0,0,n,ans,[])
        return ans