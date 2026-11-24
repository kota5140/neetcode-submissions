class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index1 = m - 1
        index2 = n - 1
        last = m + n - 1
        while index1 >= 0 or index2 >= 0:
            if index1 == -1:
                nums1[last] = nums2[index2]
                index2 -= 1
            elif index2 == -1:
                nums1[last] = nums1[index1]
                index1 -= 1
            elif nums1[index1] > nums2[index2]:
                nums1[last] = nums1[index1]
                index1 -= 1
            else:
                nums1[last] = nums2[index2]
                index2 -= 1
            last -= 1
            
