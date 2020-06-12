class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        def uniform(abs_x):
            rev = 0
            while abs_x != 0:
                mod = abs_x % 10  # 求余数
                abs_x = abs_x // 10  # 取整

                rev = rev * 10 + mod
                if rev < -pow(2, 32) or (pow(2, 31) - 1) < rev:
                    return 0
            return rev

        if x >= 0:
            return uniform(x)
        else:
            result = uniform(abs(x))
            return -result


if __name__ == '__main__':
    t = Solution()
    x = t.reverse(120)
    print(x)
