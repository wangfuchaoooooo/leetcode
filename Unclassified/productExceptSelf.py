class Solution:
    def productExceptSelf(self, nums):

        length = len(nums)
        lans = [1]*length
        rans = [1]*length
        answer = [1]*length
        lans[0] = 1
        rans[len(nums)-1] = 1
        for i in range(1,length):
            lans[i] = lans[i-1]*nums[i-1]
        for j in reversed(range(length-1)):
            rans[j] = rans[j+1]*nums[j+1]
        for i in range(length):
            answer[i] = lans[i] * rans[i]
        return answer


if __name__ == '__main__':
    s = Solution()
    nums1 = [1,2,3,4]
    re = s.productExceptSelf(nums1)
    print(re)
