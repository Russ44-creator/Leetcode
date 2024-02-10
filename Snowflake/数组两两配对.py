'''
一个数组里找到没有配对的那一个数字，比如[1,1,2,2,3,4,4]，3没有配对，输出3
保证数组里只有一个没有配对的，而且凡是配对的数字都是相邻的，说了一个无脑暴力解，问有没有更快的，
然后我说了一个二分法的解法
'''
nums = [4, 4, 1, 5, 5]
def find_single(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        # if left is even
        if (mid - left + 1) % 2 == 0:
            if nums[mid] == nums[mid - 1]:
                left = mid + 1
            else:
                right = mid - 1
        # if left is even
        else:
            if nums[mid] == nums[mid - 1]:
                right = mid
            else:
                left = mid
    return nums[left]

print(find_single(nums))