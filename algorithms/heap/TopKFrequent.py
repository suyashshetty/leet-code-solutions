import heapq
from collections import Counter

def topKFrequent(nums : list[int], k: int) -> list: 
    # Empty input
    if nums is None:
        return []
    
    count_nums = Counter(nums)
    
    # Not as many frequent elements
    if k >= len(count_nums):
        return list(count_nums.keys())
    
    num_freq = [(count_num, num) for num, count_num in count_nums.items()]
    
    heap = num_freq[:k]
    heapq.heapify(heap)
    
    for num in num_freq[k:]:
        if num[0] > heap[0][0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)
            
    return [num for _, num in heap]

def main():
    nums = [1, 2, 4, 2, 1, 4]
    k = 4
    
    print(topKFrequent(nums, k))
    
main()