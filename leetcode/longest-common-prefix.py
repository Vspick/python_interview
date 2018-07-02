class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        prefix = ""
        base = strs[0]
        for i, char in enumerate(base):
            for other_str in strs[1:]:
                if i >= len(other_str) or other_str[i] != char:
                    return prefix
            prefix += char
        return prefix