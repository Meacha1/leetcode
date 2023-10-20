class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        key = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000} # `key` is a dictionary that maps the Roman numerals to their
        s_list = list(s)
        sum = 0
        for i in range(len(s_list)):
            if s_list[i] == 'I' and i < len(s_list) - 1 and (s_list[i+1] == 'V' or s_list[i+1] == 'X'):
                sum -= key[s_list[i]]
            elif s_list[i] == 'X' and i < len(s_list) - 1 and (s_list[i+1] == 'L' or s_list[i+1] == 'C'):
                sum -= key[s_list[i]]
            elif s_list[i] == 'C' and i < len(s_list) - 1 and (s_list[i+1] == 'D' or s_list[i+1] == 'M'):
                sum -= key[s_list[i]]
            else:
                sum += key[s_list[i]]
        return(sum)
        
        
        
if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('MCMXCIV'))