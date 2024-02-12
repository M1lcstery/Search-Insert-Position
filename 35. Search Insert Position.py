class Solution(object):
    def searchInsert(self, nums, target):
        lower, upper = 0, len(nums)

        while lower < upper:
            mid = int((lower+upper)/2)
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                lower = mid +1
            else:
                upper = mid

        return lower
