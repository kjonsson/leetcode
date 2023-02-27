#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#

# @lc code=start
class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        height = len(mat)
        width = len(mat[0])

        if height * width != r * c:
            return mat
        
        results = [[0] * c for _ in range(r)]

        for h in range(height):
            for w in range(width):
                value = mat[h][w]
                index = h * width + w

                results[index // c][index % c] = value

        return results
# @lc code=end

