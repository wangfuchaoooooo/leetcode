class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = length - 2
        while i >= 0 and nums[i] >= nums[i + 1]: i -= 1 # 从右向左找到 nums[i] <= nums[i + 1]
        if i>=0:
            j = length - 1
            while j > i and nums[j] <= nums[i]: j -= 1  # 从右向左找到第一个大于nums[i]的数nums[j]
            nums[i], nums[j] = nums[j], nums[i]  # 交换两个数

        n = i+1
        m = length-1
        while n<m:  # 逆序[i+1:]
            nums[n], nums[m] = nums[m], nums[n]
            n+=1
            m-=1
        return nums


if __name__ == '__main__':
    s = Solution()
    nums1 = [4,3,2,1]
    re = s.nextPermutation(nums1)
    print(re)
