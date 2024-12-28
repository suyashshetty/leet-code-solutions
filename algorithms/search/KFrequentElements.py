from collections import Counter

def parition(branches, left, right, pivot_index):
    pivot_freq = branches[pivot_index][1]
    
    branches[pivot_index], branches[right] = branches[right], branches[pivot_index]
    curr_index = left
    for i in range(left, right):
        if branches[i][1] < pivot_freq:
            branches[curr_index], branches[i] = branches[i], branches[curr_index]
            curr_index += 1
            
    # Move pivot to final position
    branches[right], branches[curr_index] = branches[curr_index], branches[right]
    return curr_index


def quickselect(branches, left, right, k):
    if left == right:
        return
    
    pivot_index = left
    pivot_index = parition(branches, left, right, pivot_index)
    
    if k == pivot_index:
        return
    elif k < pivot_index:
        quickselect(branches, left, pivot_index - 1, k)
    else:
        quickselect(branches, pivot_index + 1, right, k)
        

def k_most_frequent(nums: list[int], k: int) -> list[int]:
    if k == 0:
        return []
    
    nums_counter = Counter(nums)
    
    if k > len(nums_counter):
        return list(set(nums))
    
    branches = list(nums_counter.items())
    n = len(branches)
    
    quickselect(branches, 0, n - 1, n - k)
    result = [branches[i][0] for i in range(n - k, n)]
    return result
    
    

def main():
    nums = [1, 2, 3, 5, 6, 1, 2, 3, 4, 1, 2, 3, 4, 7, 7, 7, 7,8]
    print(k_most_frequent(nums, 2))
    
    nums = [1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]
    print(k_most_frequent(nums, 4))
    
main()