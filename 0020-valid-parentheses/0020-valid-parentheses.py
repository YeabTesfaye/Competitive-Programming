class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_braces = {'(', '{', '['}
        close_braces = {')', '}', ']'}
        matching_braces = {'(': ')', '{': '}', '[': ']'}

        for char in s:
            if char in open_braces:
                stack.append(char)
            elif char in close_braces:
                if len(stack) == 0 or matching_braces[stack.pop()] != char:
                    return False 
        return len(stack) == 0
        