class Solution0:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                      'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        result = 0
        for _ in range(len(s)):
            i = 0
            if i == len(s) - 1:
                return result + roman_dict[s[i]]

            if (s[i] == 'I' and s[i + 1] in ['V', 'X']) \
                    or (s[i] == 'X' and (s[i + 1] in ['L', 'C'])) \
                    or (s[i] == 'C' and (s[i + 1] in ['D', 'M'])):
                result = result + roman_dict[s[i] + s[i + 1]]
                s = s[i + 2:]
            else:
                result = result + roman_dict[s[i]]
                s = s[i + 1:]
            if len(s) == 0:
                return result


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0
        for i in range(len(s) - 1):
            if dic[s[i]] < dic[s[i + 1]]:
                sum -= dic[s[i]]
            else:
                sum += dic[s[i]]
        sum += dic[s[-1]]
        return sum


if __name__ == '__main__':
    t = Solution()
    re = t.romanToInt('III')
    print(re)
