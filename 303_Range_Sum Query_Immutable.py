class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if nums:
            cumm_sum = [0] * len(nums)
            cumm_sum[0] = nums[0]
            for i in range(1,len(nums)):
                cumm_sum[i] = cumm_sum[i-1] + nums[i]
            self.cumm_sum = cumm_sum

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i==0:
            return self.cumm_sum[j]
        return self.cumm_sum[j] - self.cumm_sum[i-1]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
