#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, string1: str, string2: str) -> bool:
        if len(string1) != len(string2):
            return False
        
        string1_mapping_to_string2: dict[str, str] = {}
        string2_mapping_to_string1: dict[str, str] = {}

        for s1, s2 in zip(string1, string2):
            if s1 in string1_mapping_to_string2 and string1_mapping_to_string2[s1] != s2:
                return False

            if s2 in string2_mapping_to_string1 and string2_mapping_to_string1[s2] != s1:
                return False

            string1_mapping_to_string2[s1] = s2
            string2_mapping_to_string1[s2] = s1
            
        return True
# @lc code=end

