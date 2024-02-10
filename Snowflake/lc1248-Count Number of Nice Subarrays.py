class Solution:
    # 数学方法
    def numberOfSubarrays(self, nums, k: int) -> int:
        odd_positions = [0] 
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                odd_positions.append(i + 1) 
        odd_positions.append(len(nums) + 1) 
        
        count = 0
        for i in range(1, len(odd_positions) - k):
            count += ((odd_positions[i] - odd_positions[i - 1]) *
                      (odd_positions[i + k] - odd_positions[i + k - 1]))  # 组合数
        return count
