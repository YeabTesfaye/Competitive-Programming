class Solution:
   def threeSum(self,nums):
    nums.sort()  # Sort the input array

    n = len(nums)
    triplets = []

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicate values of nums[i]

        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                triplets.append([nums[i], nums[left], nums[right]])

                # Skip duplicate values of nums[left]
                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                # Skip duplicate values of nums[right]
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return triplets


            
            
        
        