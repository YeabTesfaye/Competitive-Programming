
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        left = 0
        right = len(nums) - 1
        
        # Find the leftmost occurrence of the target
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result[0] = mid
                right = mid - 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        # If the target is not found, return the result
        if result[0] == -1:
            return result
        
        left = 0
        right = len(nums) - 1
        
        # Find the rightmost occurrence of the target
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result[1] = mid
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return result
