class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.cache = [-1] * len(nums)
        return self.rob1(nums,len(nums)-1)

    def rob1(self,nums,i):
        if i<0:
            return 0
        if self.cache[i] !=-1:
            return self.cache[i]
        self.cache[i] = max(self.rob1(nums,i-1), nums[i] + self.rob1(nums,i-2))
        return self.cache[i]
