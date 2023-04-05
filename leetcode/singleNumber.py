def singleNumber(nums):
        xor = 0
        for num in nums:
            print(xor)
            xor ^= num
        
        return xor

nums = [4,1,2,1,2]
singleNumber(nums)