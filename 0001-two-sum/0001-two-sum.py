class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_num = {}
        for i, num in enumerate(nums):
            if num in dict_num:
                return [dict_num[num], i]
            dict_num[target-num] = i