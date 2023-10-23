class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_list = list(s)
        return(s_list)
if __name__ == '__main__':
    s = Solution()
    print(s.isValid('()[]{}'))
    print(s.isValid('(]'))