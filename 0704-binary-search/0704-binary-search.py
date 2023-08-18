class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1
        m = (h+l)//2
        
        while l <= h:
            if target == nums[m]:
                return m
            elif target < nums[m]:
                h = m - 1
                m = (h + l)//2
                continue
            elif target > nums[m]:
                l = m + 1
                m = (h + l)//2
                continue
        return -1