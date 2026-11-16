class Solution:
    def generate(self,open,close,n,ans,curr):
        if close == n:
            ans.append("".join(curr[:]))
        if open < n:
            curr.append('(')
            self.generate(open+1,close,n,ans,curr)
        if close < open:
            curr.append(')')
            self.generate(open,close+1,n,ans,curr)
        if len(curr):
            curr.pop()
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.generate(0,0,n,ans,[])
        return ans