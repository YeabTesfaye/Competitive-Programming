class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        map = {}
        maximums=[]
        for num in nums:
            map[num] = map.get(num,0)+1
        
        for num in map:
            if map[num] > len(nums)/3:
                maximums.append(num)
        return maximums
        