#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, number: int) -> bool:
        found_numbers = set()
        while True:
            next_number = sum([int(n) ** 2 for n in str(number)])

            if next_number in found_numbers:
                return False

            if next_number == 1:
                return True

            found_numbers.add(next_number)
            number = next_number
        
        return True
# @lc code=end

