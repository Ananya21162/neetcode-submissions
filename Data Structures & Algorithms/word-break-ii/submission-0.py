class Solution:
    def generate(self,i,res,sub,s,wordDict):
        if i == len(s):
            res.append(" ".join(sub[:]))
            return
        
        for j in range(i,len(s)):
            subString = s[i:j+1]
            if subString in wordDict:
                sub.append(subString)
                self.generate(j+1,res,sub,s,wordDict)
                sub.pop()
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        self.generate(0,res,[],s,wordDict)
        return res