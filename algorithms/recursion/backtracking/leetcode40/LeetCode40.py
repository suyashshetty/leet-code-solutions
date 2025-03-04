from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort candidates to help with duplicate skipping and pruning.
        candidates.sort()
        result = []
        
        # Each element in the stack is a tuple:
        # (start index, current combination, remaining target)
        stack = [(0, [], target)]
        
        while stack:
            start, curr, remain = stack.pop()
            
            # If the remaining target is exactly zero, we've found a valid combination.
            if remain == 0:
                result.append(curr)
                continue
            
            # Iterate through the candidates starting from 'start'
            for i in range(start, len(candidates)):
                # Skip duplicates: if the current candidate is the same as the previous one at this level, skip it.
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # If the candidate exceeds the remaining target, no need to proceed further.
                if candidates[i] > remain:
                    break
                
                # Push the new state onto the stack:
                # - Move to the next index (i+1) so each candidate is used at most once.
                # - Append the candidate to the current combination.
                # - Subtract the candidate's value from remain.
                stack.append((i + 1, curr + [candidates[i]], remain - candidates[i]))
                
        return result