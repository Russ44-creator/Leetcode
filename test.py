def find_min_in_v_shaped_array(arr):
    """
    Finds the minimum value in a V-shaped array where the array first decreases and then increases.
    The array may contain duplicate values.

    :param arr: List[int] - a V-shaped array
    :return: int - the minimum value in the array
    """
    if not arr:
        raise ValueError("Array is empty.")

    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        # Compare mid element with its neighbors if possible
        mid_val = arr[mid]

        # Check boundaries to avoid IndexError
        prev_val = arr[mid - 1] if mid > 0 else float('inf')
        next_val = arr[mid + 1] if mid < len(arr) - 1 else float('inf')

        if mid_val < prev_val and mid_val < next_val:
            # Found the minimum
            return mid_val
        elif mid_val > prev_val:
            # Minimum is to the left
            right = mid - 1
        elif mid_val > next_val:
            # Minimum is to the right
            left = mid + 1
        else:
            # When duplicates are present and cannot decide, move both pointers
            # This handles cases where mid_val == prev_val or mid_val == next_val
            left += 1
            right -= 1

    # After the loop, left == right
    return arr[left]

arr = [4, 4, 4, 3, 2, 1, 1, 2, 2, 3]

minimum_value = find_min_in_v_shaped_array(arr)
print("The minimum value in the array is:", minimum_value)