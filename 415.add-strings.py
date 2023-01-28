#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1_arr = list(num1)
        num2_arr = list(num2)
        carry = 0
        result = []

        while num1_arr or num2_arr or carry:
            sum1 = int(num1_arr.pop()) if num1_arr else 0
            sum2 = int(num2_arr.pop()) if num2_arr else 0
            sum = sum1 + sum2 + carry
            carry = sum // 10
            result = [str(sum % 10)] + result

        return ''.join(result)
# @lc code=end

