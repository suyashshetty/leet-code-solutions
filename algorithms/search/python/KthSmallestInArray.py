import random
import heapq
import time
from unittest.mock import right


# Quickselect function for the k-th smallest element
def quickselect(arr, k):
    def partition(arr: list, left: int, right: int, pivot: int) -> int:
        pivot_value = arr[pivot]
        arr[pivot], arr[right] = arr[right], arr[pivot]
        store_pivot = left

        for index in range(left, right):
            if arr[index] < pivot_value:
                arr[index], arr[store_pivot] = arr[store_pivot], arr[index]
                store_pivot += 1

        arr[store_pivot], arr[right] = arr[right], arr[store_pivot]
        return store_pivot

    left, right = 0, len(arr) - 1
    while True:
        k_smallest_index = partition(arr, left, right, random.randint(left, right))
        if k_smallest_index == k:
            return arr[k_smallest_index]
        elif k_smallest_index < k:
            left = k_smallest_index + 1
        else:
            right = k_smallest_index - 1


# Using heapq.nsmallest to get the k-th smallest element
def kth_smallest_with_heapq(arr, k):
    return heapq.nsmallest(k + 1, arr)[-1]


# Generating a large random list of 100000 elements
arr = [random.randint(1, 1000000) for _ in range(100000)]
k = random.randint(5000, 10000)  # Looking for the 50001-th smallest element in zero-indexed list

# Measuring runtime for Quickselect
start_time = time.time()
quickselect_result = quickselect(arr[:], k)
quickselect_time = time.time() - start_time

# Measuring runtime for heapq.nsmallest
start_time = time.time()
heapq_result = kth_smallest_with_heapq(arr[:], k)
heapq_time = time.time() - start_time

# Displaying results
print("Quickselect result:", quickselect_result)
print("Heapq result:", heapq_result)
print("Quickselect runtime:", quickselect_time, "seconds")
print("Heapq runtime:", heapq_time, "seconds")
