class Solution:
    def trap(self, height: List[int]) -> int:
        temp = 0
        left = []
        for num in height:
            if temp > 0 and temp - num > 0:
                left.append(temp - num)
            else:
                left.append(0)
            if num > temp:
                temp = num
        
        temp = 0
        right = []
        for num in height[::-1]:
            if temp > 0 and temp - num > 0:
                right.append(temp - num)
            else:
                right.append(0)
            if num > temp:
                temp = num
        right.reverse()
        
        res = 0
        for l, r in zip(left, right):
            if l !=0 and r != 0:
                res += (min(l, r))
        
        return res