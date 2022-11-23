#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        return self.my_sqrt(x, 0, x)
    
    def my_sqrt(self, x: int, start_num: int, end_num: int):
        if start_num > end_num:
            return start_num - 1
        
        mid = (start_num + end_num) // 2
        result = mid * mid
        
        if result == x:
            return mid
        
        if result > x:
            return self.my_sqrt(x, start_num, mid - 1)
        else:
            return self.my_sqrt(x, mid + 1, end_num)
# @lc code=end

print(Solution().mySqrt(6))