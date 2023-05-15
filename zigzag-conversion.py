class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
    
        rows = [''] * numRows
        row_idx = 0
        direction = 1

        for char in s:
            rows[row_idx] += char

            if row_idx == 0:
                direction = 1
            elif row_idx == numRows - 1:
                direction = -1

            row_idx += direction
        return ''.join(rows)