

def findMin(nums):
    res = nums[0]
    
    l,r = 0,len(nums) - 1
    
    while l <= r:
        if nums[l] < nums[r]:
            res = min(nums[l], res)
            break
        else:
            mid = l + r//2
            res = min(nums[mid], res)
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
    return res


nums = [3,4,5,1,2]
nums = [1]
nums = [3,4,5,1,2]
print(findMin(nums))