class Solution0:
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    print([i, j])


class Solution1:
    def twoSum(self, nums, target):
        dict_ = dict()
        for index, num in enumerate(nums):
            dict_[num] = index

        for i in range(0, len(nums)):
            result = target - nums[i]
            if result in dict_.keys() and dict_.get(result) != i:
                return [i, dict_.get(result)]


class Solution:
    def twoSum(self, nums, target):
        dict_ = dict()
        for i in range(0, len(nums)):
            result = target - nums[i]
            if result in dict_.keys():
                return [dict_.get(result), i]
            else:
                dict_[nums[i]] = i


if __name__ == '__main__':
    t = Solution()
    a, b = t.twoSum([3, 7, 3, 15], 6)
    print([a, b])
