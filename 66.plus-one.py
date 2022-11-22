#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:        
        carry = 1
        i = len(digits) - 1 

        while i >= 0:
            next_number = digits[i] + carry
            carry = next_number // 10
            digits[i] = next_number % 10
            i -= 1
            
        if carry > 0:
            return [1] + digits
        
        return digits
# @lc code=end

