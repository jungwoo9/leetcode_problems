class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        
        if len(nums) == 1:
            return nums[0]
        m = (l+r)//2
        
        while nums[l] != nums[m]:
            if nums[l] < nums[m] and nums[m] < nums[r]:
                r = m - 1
            elif nums[m] < nums[r] and nums[r] < nums[l]:
                l += 1
                r -= 1
            elif nums[r] < nums[l] and nums[l] < nums[m]:
                l = m + 1
            m = (l+r)//2
        
        return nums[l] if nums[l] < nums[r] else nums[r]