'''
Given an integer array nums, move all 0's to the end of it while 
maintaining the relative order of the non-zero elements.=

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

def moveZeros(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0 and nums[slow] == 0:
            nums[fast],nums[slow] = nums[slow],nums[fast]
            print(nums)
            
        if nums[slow] != 0:
            slow += 1
            
nums = [0,1,0,3,12]
moveZeros(nums)
        