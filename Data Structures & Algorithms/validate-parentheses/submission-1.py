class Solution:
    def isValid(self, s: str) -> bool:
        closes = {')': '(', '}': '{', ']': '['}
        stack = []
        for b in s:
            print(stack)
            if b in closes.values():
                stack.append(b)
            elif stack:
                last_val = stack.pop()
                if last_val != closes[b]:
                    return False
            else:
                return False
        if stack:
            return False
        return True
