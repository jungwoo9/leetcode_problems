class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = defaultdict(int)
        for num in nums:
            if num in count_nums:
               count_nums[num] += 1
               continue
            count_nums[num] = 1

        results = [i for i, _ in sorted(count_nums.items(), key=lambda x: x[1],  reverse=True)][:k]
        return results