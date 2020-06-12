class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        temp = 0
        i = 0
        count = 0
        while temp < length and i < length:
            if nums[i] == val:
                i = i + 1
                count = count + 1
            else:
                nums[temp] = nums[i]
                temp = temp + 1
                i = i + 1
        return length - count


if __name__ == '__main__':
    s = Solution()
    x = s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
    print(x)
