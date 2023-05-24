class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0

        #intesting question
        for i in range(len(grid)):
            column = [grid[j][i] for j in range(len(grid))]
            occurrences = grid.count(column)
            print(column)
            count += occurrences
        return count

        