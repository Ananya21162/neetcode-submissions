class Solution:
    def isPossible(self,s,i,wordDict,dp):
        if i == -1:
            return True
        if dp[i] != -1:
            return dp[i]
        for j in range(i,-1,-1):
            ss = s[j:i+1]
            if ss in wordDict:
                if self.isPossible(s,j-1,wordDict,dp):       
                    dp[i] = True
                    return True
        dp[i] = False
        return dp[i]
       
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
     
        n = len(s)
        dp = [-1]* n
        wordDict = set(wordDict)
        self.isPossible(s,n-1,wordDict,dp)
        return False if dp[n-1] == -1 else dp[n-1]