class Solution:
    def validPalindrome(self, s: str) -> bool:
        skip = 0
        i, j = 0,len(s)-1
        while i < j:
            if (s[i] != s[j]) & (skip!=0):
                return False
            elif s[i]!= s[j]:
                skip = 1
                if s[i+1] == s[j]:
                    i += 1
                elif s[i] == s[j-1]:
                    j -= 1
                else:
                    return False
            i += 1
            j -= 1
        return True

        