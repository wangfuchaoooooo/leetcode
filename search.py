class Solution:
    def search(self, nums, target):
        if not nums: return -1
        length = len(nums) - 1
        left, right = 0, length
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[length]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


if __name__ == '__main__':
    s = Solution()
    nums1 = [5,1,3]
    re = s.search(nums1, 3)
    print(re)
