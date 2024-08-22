class Solution:
    def searchRange(self, nums, target: int):
        def lowerBound(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if target <= nums[mid]:
                    right = mid - 1
                elif target > nums[mid]:
                    left = mid + 1
            return left
        def upperBound(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if target >= nums[mid]:
                    left = mid + 1
                elif target < nums[mid]:
                    right = mid - 1
            return right

        upper = upperBound(nums, target)
        low = lowerBound(nums, target)
        if upper < low:
            return [-1, -1]
        return [low, upper]

