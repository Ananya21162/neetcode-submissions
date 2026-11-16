class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        set_s = {}
        set_t = {}
        for char in s:
            set_s[char] = set_s.get(char,0) + 1
        for char in t:
            set_t[char] = set_t.get(char,0) + 1
        

        for key, value in set_s.items():
            if key not in set_t or value != set_t[key]:
                return False
        return True

