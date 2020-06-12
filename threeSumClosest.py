class Solution:
    def threeSumClosest(self, nums, target):
        length = len(nums)
        sort_nums = sorted(nums)
        ans = sort_nums[0]+sort_nums[1]+sort_nums[2]
        for i in range(length):
            L = i+1
            R = length-1
            while L<R:
                sum = sort_nums[i]+sort_nums[L]+sort_nums[R]
                if abs(sum-target) <abs(target-ans):
                    ans = sum
                if sum>target:
                    R-=1
                elif sum < target:
                    L += 1
                else:return ans
        return ans


if __name__ == '__main__':
    s = Solution()
    nums1 = [1,2,4,8,16,32,64,128]
    re = s.threeSumClosest(nums1,82)
    print(re)
