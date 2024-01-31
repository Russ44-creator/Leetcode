# https://www.1point3acres.com/bbs/thread-313877-1-1.html
class Solution:
    def findDuplicate(self, nums) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = slow
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow