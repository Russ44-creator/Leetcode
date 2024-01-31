package 面经;

import java.util.Collections;
import java.util.PriorityQueue;

public class FindMedian {
  // Find the median in an unsorted numsay
  // Method 1: Quick sort
  public static int FindMedianNum1(int[] nums) {
    int k = (int) Math.floor((nums.length - 1) / 2.0);
    return quickSort(nums, k, 0, nums.length - 1);
  }

  // 找第 k 小的元素
  public static int quickSort(int[] nums, int k, int lo, int hi) {
    int i = lo, j = hi;
    while (i < j) {
      while (i < j && nums[j] >= nums[lo])
        j--;
      while (i < j && nums[i] <= nums[lo])
        i++;
      swap(nums, i, j);
    }
    swap(nums, i, lo); // i 为 pivot所在位置
    if (i > k)
      return quickSort(nums, k, lo, i - 1);
    if (i < k)
      return quickSort(nums, k, i + 1, hi);
    return nums[i];
  }

  private static void swap(int[] nums, int i, int j) {
    int tmp = nums[i];
    nums[i] = nums[j];
    nums[j] = tmp;
  }

  // Method 2: Heap
  public static int FindMedianNum2(int[] nums) {
    int k = (int) Math.floor((nums.length - 1) / 2.0);
    PriorityQueue<Integer> heapq = new PriorityQueue<>(Collections.reverseOrder());
    for (int num : nums) {
      if (heapq.size() >= k + 1) {
        if (num < heapq.peek()) {
          heapq.poll();
          heapq.offer(num);
        }
      } else
        heapq.offer(num);
    }
    return heapq.peek();
  }

  public static void main(String[] args) {
    int[] nums = new int[] { 5, 1, 6, 7, 4, 3, 8, 9 };
    System.out.println(FindMedianNum1(nums));
    System.out.println(FindMedianNum2(nums));
  }
}
