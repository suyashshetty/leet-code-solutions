from typing import List
import random

def kth_largest_helper(arr: List, left: int, right: int, k: int) -> int:
    def partition(arr: List, left: int, right: int, pivot: int) -> int:
        pivot_value = arr[pivot]
        arr[pivot], arr[right] = arr[right], arr[pivot]
        pivot_store = left

        for index in range(left, right):
            if arr[index] < pivot_value:
                arr[index], arr[pivot_store] = arr[pivot_store], arr[index]
                pivot_store += 1

        arr[pivot_store], arr[right] = arr[right], arr[pivot_store]
        return pivot_store

    k = len(arr) - k
    while True:
        pivot_index = random.randint(left, right)
        kth_largest_idx = partition(arr, left, right, pivot_index)
        if kth_largest_idx == k:
            return arr[kth_largest_idx]
        elif kth_largest_idx < k:
            left = kth_largest_idx + 1
        else:
            right = kth_largest_idx - 1

def kth_largest(nums: List, k: int) -> int:
    return kth_largest_helper(nums, 0, len(nums) - 1, k)

input_nums = [91, 2, 5, 8, 12, 10, 77, 61]
print(kth_largest(input_nums, 1))
print(kth_largest(input_nums, 2))
