# Median of Two Sorted Arrays

# EN

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

  # RU

#   Учитывая два отсортированных массива nums1 и nums2 размера m и n соответственно, вернуть медиану двух отсортированных массивов. Общая сложность времени выполнения должна быть O(log (m+n)).

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        arr = sorted(nums1 + nums2)
        if len(arr) % 2 == 0: return (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2
        else: return arr[len(arr) // 2]