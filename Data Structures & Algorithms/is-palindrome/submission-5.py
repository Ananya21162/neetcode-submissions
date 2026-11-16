class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i <= j:
            if not self.isAlphaNum(s[i]):
                i += 1
            elif not self.isAlphaNum(s[j]):
                j -= 1
            else:
                if s[i].lower() != s[j].lower():
                    return False

                i += 1
                j -= 1
        return True
    def isAlphaNum(self, c):
        return  (ord('a') <= ord(c) <= ord('z') or 
        ord('A') <= ord(c) <= ord('Z') or 
        ord('0') <= ord(c) <= ord('9'))
     

        