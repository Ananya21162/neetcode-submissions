class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = set(["+","-","*","/"])
        for token in tokens:
            if token in operands:
                if len(stack) > 1:
                    first = stack.pop()
                    second = stack.pop()
                    if token == "+":
                        stack.append(first+second)
                    elif token == "-":
                        stack.append(second-first)
                    elif token == "*":
                        stack.append(first*second)
                    else:
                        stack.append(int(float(second)/first))
                    # print(stack)
                else:
                    return -1
            else:
                stack.append(int(token))
        
        return stack.pop()
