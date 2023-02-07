#
# @lc app=leetcode id=495 lang=python3
#
# [495] Teemo Attacking
#

# @lc code=start
class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        last_poison = 0
        result = 0
        for series in timeSeries:
            start, end = series, series + duration

            if start >= last_poison:
                result += duration
            else:
                result += end - last_poison

            last_poison = end

        return result

# @lc code=end

