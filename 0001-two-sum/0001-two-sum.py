class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        complement_dict =  {}
        complement_dict[target - nums[0]] = 0
        for i in range(1,len(nums)):
            if nums[i] in complement_dict:
                return [complement_dict[nums[i]], i]
            else:
                complement_dict[target-nums[i]] = i
        return []        