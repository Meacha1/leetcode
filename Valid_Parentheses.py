class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """


if __name__ == '__main__':
    s = Solution()
    print(s.isValid('()[]{}'))
    print(s.isValid('(]'))