#
# @lc app=leetcode id=657 lang=python3
#
# [657] Robot Return to Origin
#

# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R"):
            return True
# @lc code=end

