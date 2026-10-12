class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if len(stack) == 0:
                stack.append(char)
                continue
            if char == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(char)
            elif char == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(char)
            elif char == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        return stack == []

