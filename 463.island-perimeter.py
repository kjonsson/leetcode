#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        result = 0

        width = len(grid[0])
        height = len(grid)

        for h in range(height):
            for w in range(width):
                if grid[h][w] == 1:
                    result += 4

                    if h > 0 and grid[h - 1][w] == 1:
                        result -= 1

                    if h < height - 1 and grid[h + 1][w] == 1:
                        result -= 1
                    
                    if w > 0 and grid[h][w - 1] == 1:
                        result -= 1

                    if w < width - 1 and grid[h][w + 1] == 1:
                        result -= 1

        return result   
# @lc code=end

