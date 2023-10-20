class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        strs.sort()
        print(strs)
        str1 = strs[0]
        str2 = strs[-1]
        i = 0
        while i < len(str1) and i < len(str2):
            if str1[i] == str2[i]:
                i += 1
            else:
                break
        return str1[:i]


if __name__ == '__main__':
    strs = ["flower","flow","faight"]
    print(Solution().longestCommonPrefix(strs))