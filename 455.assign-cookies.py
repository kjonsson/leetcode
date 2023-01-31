#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
'''
    g 1 2 3 4
    s 1 2 3 4
'''

class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        greed = sorted(g)
        sizes = sorted(s)
        greed_idx, size_idx = 0, 0
        while greed_idx < len(greed) and size_idx < len(sizes):
            if greed[greed_idx] <= sizes[size_idx]:
                greed_idx += 1

            size_idx += 1

        return greed_idx
# @lc code=end

