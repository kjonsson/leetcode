#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        
        for row in range(rowIndex):
            current_level = []
            for i in range(len(result)-1):
                current_level.append(result[i] + result[i+1])
            current_level = [1] + current_level + [1]
            result = current_level
            
        return result

# @lc code=end

