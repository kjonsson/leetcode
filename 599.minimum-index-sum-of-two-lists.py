#
# @lc app=leetcode id=599 lang=python3
#
# [599] Minimum Index Sum of Two Lists
#

# @lc code=start
class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        value_to_index = {}
        for i, v in enumerate(list1):
            value_to_index[v] = i

        min_sum = len(list1) + len(list2)
        result = []

        for i, v in enumerate(list2):
            if v in value_to_index:
                if i + value_to_index[v] < min_sum:
                    min_sum = i + value_to_index[v]
                    result = [v]
                elif i + value_to_index[v] == min_sum:
                    result.append(v)

        return result
        
# @lc code=end

