class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        
        while l <= r:
            m = (l+r)//2
            print(l, r, m)
            # if l == m:
            #     break
            if matrix[m][-1] < target:
                l += 1
            elif matrix[m][0] > target:
                r -= 1
            else:
                break
        # print(l, r, m)
        # m=l
        ll, rr = 0, len(matrix[m])-1
        
        while ll <= rr:
            mm = (ll+rr)//2
            if matrix[m][mm] == target:
                return True
            if matrix[m][mm] < target:
                ll += 1
            elif matrix[m][mm] > target:
                rr -= 1
        return False