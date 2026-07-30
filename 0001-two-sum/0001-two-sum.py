class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_lookup = {}

        for i , a in enumerate(nums):

            needed_num = target - a

            if needed_num in dict_lookup:
                return [dict_lookup[needed_num] , i]

            dict_lookup[a] = i
        