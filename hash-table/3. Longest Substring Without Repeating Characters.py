class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_max = 0
        start = 0
        sub_string = ''
        
        for end in xrange(len(s)):
            if s[end] not in sub_string:
                sub_string += s[end]
            else:
                len_max = max(len_max, len(sub_string))
                while s[start] != s[end]:
                    start += 1
                start += 1
                sub_string = s[start:end+1]
        return max(len_max,len(sub_string))