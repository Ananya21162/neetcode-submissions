class Solution:
    def isPossible(self, s, i, wordSet, dp):
        if i == -1:
            return True
        
        if dp[i] != -1:
            return dp[i]
        
        for j in range(i, -1, -1):
            ss = s[j:i+1]
            if ss in wordSet:
                if self.isPossible(s, j-1, wordSet, dp):
                    dp[i] = True
                    return True
        
        dp[i] = False
        return False
       
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [-1] * n
        wordSet = set(wordDict)
        return self.isPossible(s, n-1, wordSet, dp)
