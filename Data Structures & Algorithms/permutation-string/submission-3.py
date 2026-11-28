class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        countS1 = [0]*26
        for ch in s1:
            countS1[ord(ch)-ord('a')] += 1
        countS2 = [0]*26
        for i in range(len(s1)):
            countS2[ord(s2[i])-ord('a')]+=1
        matches = 0
        for i in range(26):
            if countS1[i] == countS2[i]:
                matches += 1
            if matches == 26:
                return True
        l, r = 0, len(s1)-1
        while r < len(s2)-1:
           
            countS2[ord(s2[l])-ord('a')] -= 1
            l += 1
            r += 1
            countS2[ord(s2[r])-ord('a')] += 1
            matches = 0
            for i in range(26):
                if countS1[i] == countS2[i]:
                    matches += 1
                if matches == 26:
                    return True
            
        return False

