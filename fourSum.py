class Solution:
    def fourSum(self, nums, target):
        ans = []
        length = len(nums)
        if not nums or length <4: return ans
        sort_nums = sorted(nums) # 列表排序
        # 该方法定义四个指针 i(左端指针)，j(左二指针)，L(第三个指针)，R(最右指针)
        for i in range(length-3):
            if sort_nums[i]+sort_nums[i+1]+sort_nums[i+2]+sort_nums[i+3]>target:break
            if sort_nums[i]+sort_nums[length-3]+sort_nums[length-2]+sort_nums[length-1]<target:continue
            if i>0 and sort_nums[i] == sort_nums[i-1]: continue # 去重
            for j in range(i+1, length-2):
                if sort_nums[i] + sort_nums[j] + sort_nums[j + 1] + sort_nums[j + 2] > target: break
                if sort_nums[i] + sort_nums[j] + sort_nums[length - 2] + sort_nums[length - 1] < target: continue
                if j > i+1 and sort_nums[j] == sort_nums[j - 1]: continue  # 去重
                L = j+1
                R = length-1
                while L<R:
                    sum = sort_nums[i]+sort_nums[j]+sort_nums[L]+sort_nums[R]
                    if sum==target:
                        ans.append([sort_nums[i],sort_nums[j],sort_nums[L],sort_nums[R]])
                        while L<R and sort_nums[L]==sort_nums[L+1]: L+=1 # 去重
                        while L<R and sort_nums[R]==sort_nums[R-1]: R-=1 # 去重
                        L+=1
                        R-=1
                    elif sum<target:L+=1
                    elif sum>target:R-=1
        return ans


if __name__ == '__main__':
    s = Solution()
    nums1 = [-1,0,1,2,-1,-4]

    re = s.fourSum(nums1,-1)
    print(re)
