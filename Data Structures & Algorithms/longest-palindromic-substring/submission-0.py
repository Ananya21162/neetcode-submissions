class Solution:
    def longestPalindrome(self, s: str) -> str:
        reslen = 0
        resIdx = 0
        n = len(s)
        for i in range(n):
            l,r = i,i
            while l >=0 and r < n and s[l] == s[r]:
                if reslen < (r-l+1):
                    reslen = r-l+1
                    resIdx = l
                l -= 1
                r += 1
            l,r = i,i+1
            while l >=0 and r < n and s[l] == s[r]:
                if reslen < (r-l+1):
                    reslen = r-l+1
                    resIdx = l
                l -= 1
                r += 1
        return s[resIdx: resIdx+reslen]