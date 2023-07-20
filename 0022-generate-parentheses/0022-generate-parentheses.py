class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def check(left, right, stack):
            if left == right == n:
                res.append(stack)
            if left-right > 0 and left < n:
                check(left+1, right, stack+'(')
                check(left, right+1, stack+')')
            if left-right > 0 and left == n:
                check(left, right+1, stack+')')
            if left == right and left < n:
                check(left+1, right, stack+'(')
            
        check(1,0,'(')
        
        return res