#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_arr = list(s)

        for i in range(0, len(s_arr), 2 * k):
            s_arr[i:i + k] = reversed(s_arr[i:i + k])
        
        return ''.join(s_arr)
# @lc code=end

