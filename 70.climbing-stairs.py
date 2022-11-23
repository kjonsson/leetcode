#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        num_steps_two_back = 1
        num_steps_one_back = 2
        curr_step = num_steps_two_back + num_steps_one_back
        for i in range(3, n + 1):
            curr_step = num_steps_two_back + num_steps_one_back
            num_steps_two_back = num_steps_one_back
            num_steps_one_back = curr_step
        
        return curr_step
# @lc code=end

# print(Solution().climbStairs(4))
