class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        ops = {
            '+': lambda x, y: int(x) + int(y),
            '-': lambda x, y: int(x) - int(y),
            '*': lambda x, y: int(x) * int(y),
            '/': lambda x, y: int(int(x) / int(y)),
        }
        
        for token in tokens:
            # token is number
            if token not in ops:
                numbers.append(token) # append number
                numbers.append(None) # append None to be replaced by operator later
                continue
            
            # index of the second last None in numbers
            i = len(numbers) - numbers[:-1][::-1].index(None) - 2
            
            # do arithmetic
            res = ops[token](numbers[i-1], numbers[i+1])
            
            # replace 'num operater num' to their result
            del numbers[i-1:i+2]
            numbers.insert(i-1, res)

        return int(numbers[0])