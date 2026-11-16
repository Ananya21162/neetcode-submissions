class Solution:
 
    def decodeString(self, s: str) -> str:
        freq = []
        stack = []
        curr = ""
        k = 0
        for ch in s:
            if ch == "[":
                stack.append(curr)
                freq.append(k)
                k = 0
                curr = ""
            elif ch == "]":
                temp = curr
                curr = stack.pop()
                count = freq.pop()
                curr += temp * count
              
            elif ch.isdigit():
                k = k *10 + int(ch)
            else:
                curr += ch
            
        return curr