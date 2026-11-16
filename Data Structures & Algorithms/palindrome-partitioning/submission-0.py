class Solution:
    def isPalindrome(self,st):
        i,j = 0, len(st)-1
        while i < j:
            if st[i] != st[j]:
                return False
            i += 1
            j -= 1
        return True
    def generate(self,s,sub,res,i):
        if i == len(s):
            res.append(sub[:])
        
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if self.isPalindrome(substring):
                sub.append(substring)
                self.generate(s,sub,res,j+1)
                sub.pop()
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.generate(s,[],res,0)
        return res
        