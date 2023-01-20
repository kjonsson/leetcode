#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pass

class Solution:
    def guessNumber(self, n: int) -> int:
        def guess_number(start, end):
            middle = start + ((end - start) // 2)
            
            correct = guess(middle)
            
            if correct == 0:
                return middle
            elif correct > 0:
                return guess_number(middle + 1, end)
            else:
                return guess_number(start, middle - 1)
        return guess_number(1, n)
# @lc code=end

