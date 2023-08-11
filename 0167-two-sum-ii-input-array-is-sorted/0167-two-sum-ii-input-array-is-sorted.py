class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lst = []
        for i, num in enumerate(numbers):
            if num in lst:
                return [lst.index(num)+1, i+1]
            lst.append(target-num)