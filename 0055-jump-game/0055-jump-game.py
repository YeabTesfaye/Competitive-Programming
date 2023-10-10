class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal_post_index = len(nums) - 1

        for i in range(len(nums) - 2, -1,-1):
            if i + nums[i] >= goal_post_index:
                goal_post_index = i
        return goal_post_index == 0
        