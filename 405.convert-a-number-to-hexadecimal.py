#
# @lc app=leetcode id=405 lang=python3
#
# [405] Convert a Number to Hexadecimal
#

# @lc code=start


class Solution:
    # Write code to convert a number to hex string. Negative numbers use twos complement representation.
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        
        if num < 0:
            num += 2 ** 32
        
        result = []
        lookup = '0123456789abcdef'
        
        while num > 0:
            remainder = num % 16
            result = [lookup[remainder]] + result
            num //= 16
                        
        return ''.join(result)

# @lc code=end

