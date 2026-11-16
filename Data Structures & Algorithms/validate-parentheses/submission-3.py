class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        count =0
        for strs in s:
            if strs in ["(", "{", "["]:
                stack.append(strs)
            elif len(stack)>0 and ((strs == ")" and stack[-1] == '(') or (strs == "}" and stack[-1] == "{") or (strs == "]" and stack[-1] == "[")):
                stack.pop()
            else:
                count += 1
                continue
        print(stack)
        if len(stack)==0 and count == 0:
            return True
        else:
            return False