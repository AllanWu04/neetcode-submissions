class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_match = {')':'(', '}':'{', ']':'['}
        for c in s:
            if (c in close_match):
                if stack and stack[-1] == close_match[c]:
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)

        return not stack