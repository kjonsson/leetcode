#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        val_to_idx = defaultdict(int)

        for idx, val in enumerate(nums):
            if val in val_to_idx:
                idx_diff = idx - val_to_idx[val]
                if idx_diff <= k:
                    return True

            val_to_idx[val] = idx
            
        return False    
# @lc code=end

