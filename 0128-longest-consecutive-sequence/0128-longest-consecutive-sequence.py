class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        count = 0
        counts = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]: continue
            if nums[i] - nums[i-1] == 1:
                count += 1
                continue
            counts.append(count)
            count = 0
        counts.append(count)

        return max(counts) + 1 if nums != [] else 0