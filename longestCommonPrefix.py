class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        sorted_strs = sorted(strs, key=len)
        first_str, rest_strs = sorted_strs[0], sorted_strs[1:]
        for str in rest_strs:
            for i in range(len(first_str)):
                if first_str[i] == str[i]:
                    continue
                else:
                    if i == 0:
                        return ""
                    first_str = first_str[:i]
                break
        return first_str


if __name__ == '__main__':
    t = Solution()
    x = t.longestCommonPrefix(["flower", "flow", "flight"])
    print(x)
