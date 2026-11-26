class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in pairs.values():
                stack.append(c)
            elif c in pairs.keys():
                if not stack or stack.pop() != pairs[c]:
                    return False
            else:
                return False
        return not stack