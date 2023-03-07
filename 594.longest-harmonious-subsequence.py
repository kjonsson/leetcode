#
# @lc app=leetcode id=594 lang=python3
#
# [594] Longest Harmonious Subsequence
#

# @lc code=start
class Solution:
    def findLHS(self, nums: list[int]) -> int:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        max_len = 0
        for num in counter:
            if num + 1 in counter:
                max_len = max(max_len, counter[num] + counter[num + 1])

        return max_len
# @lc code=end

