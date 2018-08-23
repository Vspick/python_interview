class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        direct = 1
        rows = [""]*numRows  # ["" for _ in range(numRows)]
        i = 0
        for c in s:
            rows[i] += c
            i += direct
            if i == 0 or i == numRows - 1:
                direct *= -1
        return "".join(rows)
