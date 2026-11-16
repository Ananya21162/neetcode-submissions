class Solution:
    def isValid(self, s: str) -> bool:
        
        dict_map = {"(":")","{":"}","[":"]"}
        open_s = set(dict_map.keys())
        stack = []
        for i in range(len(s)):
            if s[i] in open_s:
                stack.append(s[i])
            else:
                if stack and dict_map[stack[-1]] == s[i]:
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        return True
