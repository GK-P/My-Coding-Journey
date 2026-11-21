class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        r_sum = [0] * len(nums)
        c_sum = 0

        for i in range(len(nums)):
            c_sum += nums[i]
            r_sum[i] = c_sum

        return r_sum