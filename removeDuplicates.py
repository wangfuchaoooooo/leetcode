class Solution0:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        temp = 0
        for i in range(1, len(nums)):
            if nums[temp] == nums[i]:
                continue
            else:
                temp = temp + 1
                nums[temp] = nums[i]

        return temp+1


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        temp = {}
        for i in range(len(nums)):
            if nums[temp] == nums[i]:
                continue
            else:
                temp = temp + 1
                nums[temp] = nums[i]

        return temp+1


if __name__ == '__main__':
    t = Solution()
    x = t.removeDuplicates([])
    print(x)
