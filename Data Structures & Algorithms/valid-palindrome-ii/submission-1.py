class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(left: int, right: int, isDeleted: bool) -> bool:
            while left < right:
                if s[left] != s[right]:
                    if isDeleted:
                        return False
                    result1 = checkPalindrome(left+1, right, True)
                    result2 = checkPalindrome(left, right-1, True)
                    return result1 or result2
                else:
                    left += 1
                    right -= 1
            return True

        return checkPalindrome(0, len(s)-1, False)
