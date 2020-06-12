class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True

        left_ = ['(', '[', '{']
        right_ = [')', ']', '}']
        dict_ = {'(': ')', '[': ']', '{': '}'}

        stack = []
        for i in range(len(s)):
            if s[i] in left_:
                stack.insert(0, s[i])
            elif (len(stack) == 0 or dict_[stack[0]] != s[i]) and s[i] in right_:
                return False
            else:
                if (len(stack) > 0) and (dict_[stack[0]] == s[i]):
                    stack.pop(0)

        return True if len(stack) == 0 else False


class Solution1:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        stack = []
        for i in s:
            if i == '(':
                stack.insert(0, ')')
            elif i == '[':
                stack.insert(0, ']')
            elif i == '{':
                stack.insert(0, '}')
            else:
                if len(stack) == 0 or stack.pop(0) != i:
                    return False
        return len(stack) == 0


if __name__ == '__main__':
    t = Solution()
    # 示例1:
    # 输入: "()"
    # 输出: true

    # 示例2:
    # 输入: "()[]{}"
    # 输出: true

    # 示例3:
    # 输入: "(]"
    # 输出: false

    # 示例4:
    # 输入: "([)]"
    # 输出: false

    # 示例5:
    # 输入: "{[]}"
    # 输出: true
    x = t.isValid("([)")
    print(x)
