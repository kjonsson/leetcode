#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        
        curr_range = [nums[0], nums[0]]
        result = []
        for prev, curr in zip(nums[:-1], nums[1:]):            
            if curr - prev == 1:
                curr_range[1] = curr
                continue
                
            result.append(curr_range.copy())
            curr_range = [curr, curr]
            
        result.append(curr_range)
        
        return [f'{a}->{b}' if a != b else f'{a}' for [a, b] in result]
# @lc code=end

