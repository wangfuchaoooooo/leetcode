"""
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。

示例 1:
nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0

示例 2:
nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        median_num = (len1 + len2) // 2
        temp = []
        i = 0
        j = 0
        n = 0
        while n < (median_num + 1):
            if j >= len2:
                temp.extend(nums1[i:(median_num - n + 1 + i)])
                break
            if i >= len1:
                temp.extend(nums2[j:(median_num - n + 1 + j) ])
                break
            if nums1[i] > nums2[j]:
                temp.append(nums2[j])
                j = j + 1
                n = n + 1
            elif nums1[i] < nums2[j]:
                temp.append(nums1[i])
                i = i + 1
                n = n + 1
            elif nums1[i] == nums2[j]:
                temp.append(nums1[i])
                i = i + 1
                n = n + 1
                if n >= (median_num + 1):
                    break
                temp.append(nums2[j])
                j = j + 1
                n = n + 1
                if n >= (median_num + 1):
                    break
        if (len1 + len2) % 2 == 0:
            return (temp[-1] + temp[-2]) / 2
        else:
            return temp[-1]


if __name__ == '__main__':
    s = Solution()
    nums1 = [1,3,5,7]
    nums2 = [2,4,6,9]
    re = s.findMedianSortedArrays(nums1, nums2)
    print(re)
