#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray:

    def __init__(self, nums: list[int]):
        self.sums_up_to_index = []
        sum_ = 0
        for num in nums:
            sum_ += num
            self.sums_up_to_index.append(sum_)

    def sumRange(self, i: int, j: int) -> int:
        if i < 1:
            return self.sums_up_to_index[j]

        return self.sums_up_to_index[j] - self.sums_up_to_index[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

a = NumArray([-2, 0, 3, -5, 2, -1])
print(a.sumRange(0, 2))