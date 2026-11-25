class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        # -4 -1 -1 0 1 2
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            elif nums[i] > 0:
                break
            left = i+1
            right = n-1
            target = -nums[i]
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    ans.append([nums[left], nums[i], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return ans