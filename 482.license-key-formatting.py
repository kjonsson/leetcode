#
# @lc app=leetcode id=482 lang=python3
#
# [482] License Key Formatting
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()

        if len(s) == 0:
            return ''

        remainder = len(s) % k

        result = s[:remainder]
        s = s[remainder:]

        while s:
            result += '-' + s[:k]
            s = s[k:]

        return result if result[0] != '-' else result[1:]


# @lc code=end

