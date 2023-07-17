class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '[':']', '{':'}'}
        lst = [0]
        for bracket in s:
            if lst[-1] in brackets and brackets[lst[-1]] == bracket:
                del lst[-1]
                continue
            lst.append(bracket)
        return [0] == lst