from typing import List
from functools import lru_cache

class Solution:
    
    # Time Complexity: O(n * target) where n is the number of elements in nums and target is the target sum.
    # Space Complexity: O(target) due to recursion stack and memoization cache.
    def combinationSum4_recursion(self, nums: List[int], target: int) -> int:
        # Using LRU cache for memoization.
        @lru_cache(maxsize=None)
        def backtrack(remain: int) -> int:
            # Base case: if remain is zero, one valid combination is found.
            if remain == 0:
                return 1
            count = 0
            # For each number, if it can be used (remain >= num), recurse.
            for num in nums:
                if remain >= num:
                    count += backtrack(remain - num)
            return count

        return backtrack(target)
    
    # Time Complexity: O(n * target) where n is the number of elements in nums and target is the target sum.
    # Space Complexity: O(target) for the dp table and recursion/iteration overhead.
    def combinationSum4_dynamic(self, nums: List[int], target: int) -> int:
        # dp[i] will hold the number of combinations that add up to i.
        dp = [0] * (target + 1)
        dp[0] = 1  # Base case: one way to sum to 0
        
        # Build the dp table from 1 to target.
        for total in range(1, target + 1):
            for num in nums:
                if total >= num:
                    dp[total] += dp[total - num]
                    
        return dp[target]
    
    # Time Complexity: O(n * target) under typical assumptions, where n is the number of elements in nums.
    # Space Complexity: O(target) for storing memo and explicit stack (in worst-case, similar to recursion depth).
    def combinationSum4_stack(self, nums: List[int], target: int) -> int:
        # Base memo: There is exactly one way to reach a sum of 0.
        memo = {0: 1}
        
        # Explicit stack to simulate DFS.
        # We'll push "remain" values that need to be computed.
        stack = []
        if target != 0:
            stack.append(target)
        
        while stack:
            remain = stack[-1]  # Peek at the top of the stack.
            
            # If "remain" is already computed in memo, we can remove it.
            if remain in memo:
                stack.pop()
                continue
            
            all_children_computed = True
            temp_sum = 0
            
            # Iterate over each number to compute contributions from subproblems.
            for num in nums:
                if remain >= num:
                    child = remain - num
                    # If the child is not computed, push it onto the stack.
                    if child not in memo:
                        all_children_computed = False
                        stack.append(child)
                    else:
                        temp_sum += memo[child]
            
            # If all subproblems (children) for "remain" are computed, store the result.
            if all_children_computed:
                memo[remain] = temp_sum
                stack.pop()
        
        return memo[target]

# Example Usage:
solution = Solution()
print(solution.combinationSum4_recursion([1, 2, 3], 4))  # Expected Output: 7
print(solution.combinationSum4_dynamic([1, 2, 3], 4))      # Expected Output: 7
print(solution.combinationSum4_stack([1, 2, 3], 4))          # Expected Output: 7
