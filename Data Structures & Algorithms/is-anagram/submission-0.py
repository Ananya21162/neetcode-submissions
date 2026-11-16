class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count_s = {}
        count_t = {}
        for value in s:
            if value in count_s:
                count_s[value] += 1
            else:
                count_s.update({value:1})
        for value in t:
            if value in count_t:
                count_t[value] += 1
            else:
                count_t.update({value:1})
        
        
        if count_s == count_t:
            return True
        else:
            return False
            
         
        