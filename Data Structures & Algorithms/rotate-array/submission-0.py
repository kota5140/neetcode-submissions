class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1 2 3 4 5 => 3 4 5 1 2: 3
        # 5 4 3 2 1 => 
        def reverseArray(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        n = len(nums)
        rot = k % n
        reverseArray(0, n-1)
        reverseArray(0, rot-1)
        reverseArray(rot, n-1)

        