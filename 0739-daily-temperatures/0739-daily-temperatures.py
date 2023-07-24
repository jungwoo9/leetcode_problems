class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            temp = temperatures[i]
            while stack and stack[-1][0] < temp:
                res[stack[-1][1]] = i-stack[-1][1]
                # res.insert(stack[-1][1], i-stack[-1][1])
                # del res[stack[-1][1]+1]
                stack.pop()
            
            stack.append([temp, i])
            
        return res
        
#         res = []
        
#         for i in range(len(temperatures)-1):
#             temp = temperatures[i]
#             new = 0
#             for j, temp_future in enumerate(temperatures[i+1:]):
#                 if temp < temp_future:
#                     new = j + 1
#                     break
#             res.append(new)
        
#         return res + [0]