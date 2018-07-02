class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        substr = ""
        for c in s:
            loc = substr.find(c)
            if loc == -1:
                substr += c
                max_len = max(max_len, len(substr))
            else:
                substr = substr[loc + 1:] + c
        return max_len


class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        i = 0
        char_map = dict()
        for j, c in enumerate(s):
            if c not in char_map or char_map[c] < i:
                max_len = max(max_len, j - i + 1)
            else:
                i = char_map[c] + 1
            char_map[c] = j
        return max_len
