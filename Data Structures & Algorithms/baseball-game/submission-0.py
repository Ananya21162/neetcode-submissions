class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                first = stack[-1]
                second = stack[-2]
                stack.append(first+second)
            elif op == "D":
                prev = stack[-1]
                stack.append(2*prev)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)