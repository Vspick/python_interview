class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        row_num = len(matrix)
        col_num = len(matrix[0])
        l = 0
        r = row_num * col_num - 1
        while l <= r:
            m = (l + r) / 2
            m_row = m // col_num
            m_col = m % col_num
            v = matrix[m_row][m_col]
            if v == target:
                return True
            elif v < target:
                l = m + 1
            else:
                r = m - 1
        return False
