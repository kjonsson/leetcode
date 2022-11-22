#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for v in s:
            if v in ['(', '{', '[']:
                stack.append(v)
                continue
            
            if len(stack) == 0:
                return False
                
            popped = stack.pop()
            
            if popped == '(' and v != ')':
                return False
            
            if popped == '{' and v != '}':
                return False
            
            if popped == '[' and v != ']':
                return False
            
        return len(stack) == 0
# @lc code=end

