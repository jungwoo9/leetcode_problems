class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s.lower().replace(' ', '').translate(str.maketrans('', '', string.punctuation)))
        if len(s) == 0 or len(s) == 1: return True
        return s[:len(s)//2] == s[ceil(len(s)/2):][::-1]
        # return False