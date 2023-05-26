class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                currStr = ''
                while stack[-1] != '[':
                    currStr  = stack.pop() + currStr
                stack.pop()
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k 
                stack.append(int(k)*currStr)
        return "".join(stack)


        