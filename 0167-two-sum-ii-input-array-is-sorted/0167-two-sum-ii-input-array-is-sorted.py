class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # lst = []
        # for i, num in enumerate(numbers):
        #     if num in lst:
        #         return [lst.index(num)+1, i+1]
        #     lst.append(target-num)
        
        l, r = 0, len(numbers)-1
        
        while l < r:
            two_sum = numbers[l] + numbers[r]
            
            if two_sum < target:
                l += 1
            elif two_sum > target:
                r -= 1
            else:
                return [l+1, r+1]