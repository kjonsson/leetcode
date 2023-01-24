#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#

# @lc code=start
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        '''
            I have 4 bits for hours and 6 bits for minutes
            I can use a bit mask to generate all possible combinations
        '''
        res = []
        for h in range(12):
            for m in range(60):
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    res.append(f'{h}:{m:02}')

        return res
# @lc code=end

