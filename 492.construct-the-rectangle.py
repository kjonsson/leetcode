#
# @lc app=leetcode id=492 lang=python3
#
# [492] Construct the Rectangle
#

# @lc code=start
class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        width = int(area ** 0.5)
        for w in range(width, 1, -1):
            if area % w == 0:
                return [area // w, w]
            
        return [area, 1]
# @lc code=end

