class Solution:
    def isHappy(self, n: int) -> bool:
        def square(num):
            
            ans = 0
            while num > 0:
                rem = num % 10
                ans += rem*rem 
                num //= 10
            return ans
        
        slow,fast = n,n 
        
        while True:
            fast = square(square(fast))
            slow = square(slow)
            
            if slow == fast:
                break 
        return slow == 1 