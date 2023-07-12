class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix = prefix * nums[i]
        for j in range(len(nums)):
            answer[len(nums)-j-1] = answer[len(nums)-j-1] * postfix
            postfix = postfix * nums[len(nums)-j-1]
        return answer