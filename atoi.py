class Solution:
    def myAtoi(self, s: str) -> int:
            # Remove leading and trailing whitespaces
            s = s.strip()

            # Check if the string is empty
            if len(s) == 0:
                return 0

            # Check if the first character is a sign (+/-)
            if s[0] == '+' or s[0] == '-':
                sign = -1 if s[0] == '-' else 1
                s = s[1:]  # Remove the sign from the string
            else:
                sign = 1

            # Convert characters to digits until a non-digit character is encountered
            digits = '0123456789'
            num = 0
            i = 0
            while i < len(s) and s[i] in digits:
                num = num * 10 + int(s[i])
                i += 1

            # Apply the sign and handle integer overflow
            num = sign * num
            num = max(min(num, 2**31 - 1), -2**31)

            return num