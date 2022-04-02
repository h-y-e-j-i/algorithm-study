# 189
# https://leetcode.com/problems/rotate-array/

class Solution(object):
    def rotate(self, nums, k):
        k = k%len(nums)
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]