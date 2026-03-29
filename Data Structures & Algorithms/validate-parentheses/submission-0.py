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
        print(stack)
        if len(stack) > 0:
            return False
        return True
