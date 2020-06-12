class Solution0:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            num_str = str(x)
            num_len = len(num_str)
            num_dict = {}
            for index, num in enumerate(num_str):
                num_dict[index] = num

            for i in range(num_len // 2):
                if num_dict[i] != num_dict[num_len - i - 1]:
                    return False
            return True


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        else:
            semi_num = 0
            while x > semi_num:
                mod = x % 10  # 求余数
                x = x // 10  # 取整
                semi_num = semi_num*10 + mod

            return (x == semi_num) or (semi_num // 10 == x)


if __name__ == '__main__':
    t = Solution()
    bool_ = t.isPalindrome(123321)
    print(bool_)
