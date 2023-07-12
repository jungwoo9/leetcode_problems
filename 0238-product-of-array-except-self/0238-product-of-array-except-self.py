class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0
        for num in nums:
            if num==0:
                zeros += 1
                continue
            product = product * num

        if zeros >= 2:
            answer = [0] * len(nums)
        elif zeros == 1:
            answer = [0]*len(nums)
            answer[nums.index(0)] = product
        else:
            answer = [int(product/denom) for denom in nums]
        return answer