
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        wordDict = set(dictionary)
        dp = [-1]*(len(s))
        def dfs(i):
            if len(s) == i:
                return 0
            if dp[i] != -1:
                return dp [i]
            res = 1+dfs(i+1)
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if sub in wordDict:
                    res = min(res,dfs(j+1))
            dp[i] = res
            return res
        return dfs(0)