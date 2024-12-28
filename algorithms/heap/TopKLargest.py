import heapq

def topKLargest(nums : list[int], k: int) -> list:
    if k >= len(nums):
        return nums
    
    heap = nums[:k]
    heapq.heapify(heap)
    
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)
            
    return heap

def main():
    nums = [3, 15, 11, 1, 78, 5, 0, 2]
    k = 4
    
    print(topKLargest(nums, k))
    
main()