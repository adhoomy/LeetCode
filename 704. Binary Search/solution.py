class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r)/2
            if nums[m] == target:
                return m
            if target < nums[m]:
                r = m-1
            if target > nums[m]:
                l = m+1
        return -1