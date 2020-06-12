class Solution:
    def search_left_id(self,nums,target,left):
        l = 0
        r = len(nums)
        while l<r:
            mid = (l+r)//2
            if nums[mid] > target or (left and nums[mid]==target):
                r = mid
            else:
                l = mid+1
        return l

    def searchRange(self, nums, target):
        left_id = self.search_left_id(nums, target, True)
        if left_id == len(nums) or nums[left_id] != target:
            return [-1,-1]
        return [left_id, self.search_left_id(nums,target,False)-1]


if __name__ == '__main__':
    s = Solution()
    nums1 = []
    re = s.searchRange(nums1, 3)
    print(re)
