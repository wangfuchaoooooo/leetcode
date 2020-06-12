'''
标签：数组遍历
首先对数组进行排序，排序后固定一个数 nums[i]，再使用左右指针指向 nums[i]后面的两端，
   数字分别为 nums[L] 和 nums[R]，计算三个数的和 sum 判断是否满足为 0，满足则添加进结果集
如果 nums[i]大于 0，则三数之和必然无法等于 0，结束循环
如果 nums[i] == nums[i-1]，则说明该数字重复，会导致结果重复，所以应该跳过
当 sum = 0 时，nums[L] = nums[L+1] 则会导致结果重复，应该跳过，L++
当 sum = 0 时，nums[R] = nums[R−1] 则会导致结果重复，应该跳过，R−−
时间复杂度：O(n^2)

'''

class Solution:
    def threeSum(self, nums):
        import numpy as np
        ans = []
        length = len(nums)
        if length <3: return ans
        sort_nums = sorted(nums)
        print(sort_nums)
        for i in range(length):
            if sort_nums[i]>0: break
            if i>0 and sort_nums[i] == sort_nums[i-1]: continue # 去重
            L = i+1
            R = length-1
            while L<R:
                sum = sort_nums[i]+sort_nums[L]+sort_nums[R]
                if sum==0:
                    ans.append([sort_nums[i],sort_nums[L],sort_nums[R]])
                    while L<R and sort_nums[L]==sort_nums[L+1]: L+=1 # 去重
                    while L<R and sort_nums[R]==sort_nums[R-1]: R-=1 # 去重
                    L+=1
                    R-=1
                elif sum<0:L+=1
                elif sum>0:R-=1
        return ans


if __name__ == '__main__':
    s = Solution()
    nums1 = [-1, 0, 1, 2, -1, -4]
    re = s.threeSum(nums1)
    print(re)
