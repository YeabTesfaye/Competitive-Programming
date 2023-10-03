class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        counter_dic = {}
        for num in nums:
            if num in counter_dic:
                counter_dic[num] += 1
            else:
                counter_dic[num] = 1
        return max(counter_dic, key=counter_dic.get)
        
        