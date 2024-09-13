import time
import tracemalloc
import sys

# Set a new recursion limit
sys.setrecursionlimit(1500)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#------------------------------------------------------------
from typing import Optional

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0

        def helperSum(node: Optional[TreeNode], low: int, high: int) -> int:
            if node is None:
                return 0
            
            leftSum, rightSum = 0, 0
            
            if node.val > low:
                leftSum = helperSum(node.left, low, high)
            if node.val < high:
                rightSum = helperSum(node.right, low, high)
            
            currentSum = node.val if low <= node.val <= high else 0

            return currentSum + leftSum + rightSum

        return helperSum(root, low, high)
    
#------------------------------------------------------------



def format_memory_usage(current, peak):
    if current < 10**6:
        current_usage = f"{current / 10**3:.3f} KB"
    else:
        current_usage = f"{current / 10**6:.3f} MB"
    
    if peak < 10**6:
        peak_usage = f"{peak / 10**3:.3f} KB"
    else:
        peak_usage = f"{peak / 10**6:.3f} MB"
    
    return current_usage, peak_usage

def run_tests():
    solution = Solution()

    # Helper function to create a binary search tree
    def insert_into_bst(root, val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = insert_into_bst(root.left, val)
        else:
            root.right = insert_into_bst(root.right, val)
        return root

    # Edge Test Case 1: Empty Tree
    root = None
    low, high = 0, 100
    expected_output = 0
    
    tracemalloc.start()
    start_time = time.time()
    result = solution.rangeSumBST(root, low, high)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    current_usage, peak_usage = format_memory_usage(current, peak)
    print(f"Edge Test Case 1 passed in {end_time - start_time:.6f} seconds")
    print(f"Current memory usage: {current_usage}; Peak: {peak_usage}\n")

    # Edge Test Case 2: Single Node Tree
    root = TreeNode(10)
    low, high = 5, 15
    expected_output = 10
    
    tracemalloc.start()
    start_time = time.time()
    result = solution.rangeSumBST(root, low, high)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    current_usage, peak_usage = format_memory_usage(current, peak)
    print(f"Edge Test Case 2 passed in {end_time - start_time:.6f} seconds")
    print(f"Current memory usage: {current_usage}; Peak: {peak_usage}\n")

    root = None
    values = range(1, 1001)  # Insert 999 nodes
    for val in values:
        root = insert_into_bst(root, val)

    low, high = 500, 1000
    expected_output = sum(range(500, 1001))

    tracemalloc.start()
    start_time = time.time()
    result = solution.rangeSumBST(root, low, high)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    current_usage, peak_usage = format_memory_usage(current, peak)
    print(f"Large Test Case passed in {end_time - start_time:.6f} seconds")
    print(f"Current memory usage: {current_usage}; Peak: {peak_usage}\n")

run_tests()
