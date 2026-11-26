class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if not stack or stack.pop() != hashMap[c]:
                    return False
        return not stack