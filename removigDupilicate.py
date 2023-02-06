

def removigDuplicate(nums):
    l = 1
    for r in range(1,len(nums)):
        if nums[r] != nums[r-1]:
            l += 1
            nums[l] = nums[r]
    print(nums)
    return l
                             
nums = [0,0,1,1,1,2,2,3,3,4]
