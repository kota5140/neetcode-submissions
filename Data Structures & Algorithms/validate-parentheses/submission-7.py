class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in hashMap.values():
                stack.append(c)
            elif c in hashMap.keys():
                if not stack or stack.pop() != hashMap[c]:
                    return False
            else:
                return False
        return not stack