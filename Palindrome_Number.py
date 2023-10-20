class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        x_str_rev = x_str[::-1]
        if x_str == x_str_rev:
            return True
        return False

if __name__ == '__main__':
    x = 'abc'
    print(Solution().isPalindrome(x))
