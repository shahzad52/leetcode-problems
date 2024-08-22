''' Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.'''

class Solution(object):
    def twoSum(self, nums, target):
        for j in range (0,len(nums)-1):
            for i in range (j,len(nums)-1):
                if nums[j]+nums[i+1] == target:
                    return j,i+1
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """   
