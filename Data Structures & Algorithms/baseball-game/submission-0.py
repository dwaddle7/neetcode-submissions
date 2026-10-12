class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                left = stack[-2]
                right = stack[-1]
                new = left + right
                stack.append(new)
            elif op == "C":
                stack.pop()
            elif op == "D":
                stack.append(2 * stack[-1])
            else: # it's a string of an int
                stack.append(int(op))
        return sum(stack)