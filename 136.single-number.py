#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution(object):
    def singleNumber(self, nums: list[int]) -> int:
        store = set()
        for num in nums:
            if num in store:
                store.remove(num)
            else:
                store.add(num)
                
        return list(store)[0]
# @lc code=end

