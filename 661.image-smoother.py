#
# @lc app=leetcode id=661 lang=python3
#
# [661] Image Smoother
#

# @lc code=start
class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        def get_average_around_point(h: int, w: int, img: list[list[int]]) -> int:
            total = 0
            count = 0

            width = len(img[0])
            height = len(img)

            for h_curr in range(h-1, h+2):
                for w_curr in range(w-1, w+2):
                    if 0 <= h_curr < height and 0 <= w_curr < width:
                        total += img[h_curr][w_curr]
                        count += 1
            return total // count
        
        width = len(img[0])
        height = len(img)

        result = [[0 for _ in range(width)] for _ in range(height)]

        for h in range(height):
            for w in range(width):
                result[h][w] = get_average_around_point(h, w, img)

        return result
# @lc code=end

