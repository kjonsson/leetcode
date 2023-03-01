#
# @lc app=leetcode id=575 lang=python3
#
# [575] Distribute Candies
#

# @lc code=start
class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        number_of_candy_types = len(set(candyType))
        number_of_candies_to_eat = len(candyType) // 2

        return min(number_of_candy_types, number_of_candies_to_eat)
# @lc code=end

