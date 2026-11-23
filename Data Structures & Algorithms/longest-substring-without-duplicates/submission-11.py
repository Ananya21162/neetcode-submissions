class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        l, r = 0,0
        ll = 0
        for ch in s: 
            ll = max(ll, r -l)    
            while ch in unique:
                unique.remove(s[l])
                l += 1
            unique.add(ch)
            r += 1
        ll = max(ll, r -l)    
        return ll
                
