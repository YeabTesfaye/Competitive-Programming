class Solution:
    def reverse(self, x: int) -> int:
        # Check if the input is negative
        if x < 0:
            sign = -1
            x = abs(x)
        else:
            sign = 1
        
        # Reverse the integer
        reversed_num = 0
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        
        # Handle integer overflow
        if reversed_num > 2**31 - 1:
            return 0
        
        return sign * reversed_num