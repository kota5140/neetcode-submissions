class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(temp: List[int], start: int, end: int):
            if start >= end:
                return
            i, j = start, end
            pivot = temp[(start + end) // 2]
            while i <= j:
                while temp[i] < pivot:
                    i += 1
                while temp[j] > pivot:
                    j -= 1
                if i <= j:
                    temp[i], temp[j] = temp[j], temp[i]
                    i += 1
                    j -= 1
            quicksort(temp, start, j)
            quicksort(temp, i, end)
            return temp
        quicksort(nums, 0, len(nums)-1)
        return nums
