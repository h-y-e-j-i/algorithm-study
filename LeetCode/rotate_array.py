class Solution(object):
    def rotate(self, nums, k):
        right_list = nums[len(nums)-k:]
        left_list = nums[:len(nums)-k]
        return right_list+left_list

solution = Solution()
print(solution.rotate([1,2,3,4,5,6,7], 3))