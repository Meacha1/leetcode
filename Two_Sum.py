class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums and nums.index(diff) != i: # `nums.index(diff)` is finding the index of the element `diff` in the
                return [i, nums.index(diff)]           # list `nums`. It returns the first occurrence of `diff` in `nums`.                

if __name__ == '__main__':
    nums = [2,15,11,7]
    target = 9
    print(Solution().twoSum(nums, target))