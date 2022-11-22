#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = []
        
        if len(b) < len(a):
            a, b = b, a
        
        a_idx = len(a) - 1
        b_idx = len(b) - 1
        while a_idx >= 0 or b_idx >= 0:
            total = carry 
            if a_idx >= 0:
                total += int(a[a_idx])
                a_idx -= 1
            if b_idx >= 0:
                total += int(b[b_idx])
                b_idx -= 1
            
            result = [total % 2] + result 
            carry = total // 2
        
        if carry > 0:
            result = [1] + result

        return ''.join([str(x) for x in result])
                
# @lc code=end

