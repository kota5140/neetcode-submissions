class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(self, left: int, right: int, isDeleted: bool) -> bool:
            while left < right:
                if not s[left].isalnum():
                    left += 1
                elif not s[right].isalnum():
                    right -= 1
                elif s[left] != s[right]:
                    if isDeleted:
                        return False
                    result1 = checkPalindrome(self, left+1, right, True)
                    result2 = checkPalindrome(self, left, right-1, True)
                    if result1 or result2:
                        return True
                    else:
                        return False
                else:
                    left += 1
                    right -= 1
            return True

        return checkPalindrome(self, 0, len(s)-1, False)
