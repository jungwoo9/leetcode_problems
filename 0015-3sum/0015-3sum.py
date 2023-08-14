class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
#         l, m, r = 0, 1, 2
#         res = []
#         while True:
#             if nums[l] + nums[m] + nums[r] == 0:
#                 sorted_res = sorted([nums[l], nums[m], nums[r]])
#                 if sorted_res not in res:
#                     res.append(sorted_res)
#             if len(nums)-1 == r and len(nums)-2 == m and len(nums)-3 == l:
#                 break
#             elif len(nums)-1 == r and len(nums)-2 == m:
#                 l += 1
#                 m = l + 1
#                 r = m + 1
#             elif len(nums)-1 == r:
#                 m += 1
#                 r = m + 1
#             else:
#                 r += 1
            
#         return res
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                
                if a + nums[l] + nums[r] > 0:
                    r -= 1
                elif a + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
        
        return res