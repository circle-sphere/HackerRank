# 2021-01-13
# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]
