#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        def binary_search(start: int, end: int, target: int):
            mid = start + ((end - start) // 2)
            
            if start == end:
                return mid ** 2 == target
            if start > end:
                return False
            
            squared = mid ** 2
            if squared == num:
                return True
            elif squared > num:
                end = mid - 1
            else:
                start = mid + 1
                
            return binary_search(start, end, target)
        return binary_search(0, num, num)
# @lc code=end

