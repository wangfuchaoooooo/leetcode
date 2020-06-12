class Solution:
    def maxArea(self, height):
        l,r = 0, len(height) - 1
        max_area = 0
        while l < r:
            xl = height[l]
            xr = height[r]
            width = r-l
            temp = min(xl, xr) * width
            max_area = max(temp, max_area)
            if xl >= xr:
                r -= 1
            else:
                l += 1
        return max_area



if __name__ == '__main__':
    s = Solution()
    nums1 = [1,0,0,3]
    re = s.maxArea(nums1)
    print(re)
