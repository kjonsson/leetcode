#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s: str):
        s = ''.join([x.lower() for x in s if x.isalnum()])
        
        start = 0
        end = len(s) - 1

        while start <= end:
            if s[start] != s[end]:
                return False

            start += 1
            end -= 1
            
        return True
        
        
# @lc code=end

