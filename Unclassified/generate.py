class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        b = [1]
        for _ in range(numRows):
            yield b
            b = [1] + [b[i] + b[i + 1] for i in range(len(b) - 1)] + [1]
        return b


if __name__ == '__main__':
    t = Solution()
    a = t.generate(4)
    for i in a:
        print(i)
