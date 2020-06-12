class Solution:

    def _myPowHelper(x_, n_):
        if n_ == 0:
            return 1
        half = Solution._myPowHelper(x_, n_ // 2)
        if n_ % 2 == 0:
            return half * half
        else:
            return half * half * x_

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n >= 0:
            return Solution._myPowHelper(x, n)
        else:
            return 1 / Solution._myPowHelper(x, abs(n))


if __name__ == '__main__':
    t = Solution()
    x = t.myPow(2, -4)
    pow()
    print(x)
