class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(":
                stack.append("x")
            elif c == ")":
                if not stack:
                    return False
                x = stack.pop()
                if x != "x":
                    return False
            elif c == "[":
                stack.append("y")
            elif c == "]":
                if not stack:
                    return False
                y = stack.pop()
                if y != "y":
                    return False
            elif c == "{":
                stack.append("z")
            elif c == "}":
                if not stack:
                    return False
                z = stack.pop()
                if z != "z":
                    return False
            else:
                return False
        if stack:
            return False
        return True