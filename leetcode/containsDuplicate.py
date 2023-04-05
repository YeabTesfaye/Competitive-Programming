'''
Given an integer array nums, return true if any
value appears at least twice in the array, and return false if every element is distinct.
'''

def containsDuplicate(nums):
    
    haseset = set()
    
    for n in nums:
        if n in haseset:
            return True
        haseset.add(n)
    return False


# Input: nums = [1,2,3,1]
# Output: true
nums = [1,2,3,1]
print(containsDuplicate(nums))